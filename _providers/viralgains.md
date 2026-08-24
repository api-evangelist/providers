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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/viralgains-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://viralgains.com
- group: company
  title: ''
  type: Blog
  url: https://www.viralgains.com/resources/press-blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.viralgains.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.viralgains.com/terms-conditions/
- group: operate
  title: ''
  type: Support
  url: https://www.viralgains.com/contact-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ViralGains
- group: build
  title: ''
  type: Packages
  url: packages/viralgains-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/viralgains-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/viralgains-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.viralgains.com/ccpa-compliance/
- group: commercial
  title: ''
  type: Plans
  url: plans/viralgains-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/viralgains-rate-limits.yml
coverage:
  checked: '2026-08-12'
  detail: ViralGains runs a WordPress marketing site and nothing else — api., developer., developers. and docs.viralgains.com are all NXDOMAIN, the 41-URL Yoast page sitemap contains no developer, API, docs or pricing page, and the FAQ routes all implementation questions to 800-501-2763 and hello@viralgains.com because media is activated through third-party DSPs and SSPs rather than a ViralGains API.
  evidence:
  - status: 0
    url: https://api.viralgains.com/
  - status: 404
    url: https://www.viralgains.com/openapi.json
  - status: 404
    url: https://www.viralgains.com/.well-known/agent-card.json
  - status: 404
    url: https://www.viralgains.com/llms.txt
  - status: 404
    url: https://www.viralgains.com/pricing
  - status: 200
    url: https://www.viralgains.com/page-sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: ViralGains is an advertising technology platform that collects consumer feedback directly within digital ad units as zero-party data, then combines that real-time, consented consumer input with its VoiceAlike AI to build higher-quality audiences and deliver more relevant, privacy-respecting advertising for brands and agencies. The platform spans zero-party data collection, brand lift measurement, and a dedicated health and pharma offering (VG Health). ViralGains was surfaced as a portfolio company of 500 Global and added to the API Evangelist network. As of this enrichment pass the company publishes a marketing and product website but no public developer program, API documentation, or machine-readable API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/viralgains.png
layout: provider
modified: '2026-08-12'
name: ViralGains
nav: Providers
network: true
overview: 'ViralGains is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Zero-Party Data, and Marketing.


  ViralGains'' developer surface includes engineering blog, support, and 11 more developer resources.'
plans:
- name: Viralgains Plans Pricing
  plan_count: 0
  slug: viralgains-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Viralgains Rate Limits
  slug: viralgains-rate-limits
score:
  band: emerging
  composite: 18.5
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 18.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 38.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Viralgains Domain Security
  slug: viralgains-domain-security
  summary_line: TLSv1.3 · DMARC
slug: viralgains
tags:
- Company
- Advertising
- AdTech
- Zero-Party Data
- Marketing
- Brand Lift
- Consumer Insights
- Health and Pharma
website: https://viralgains.com
---
