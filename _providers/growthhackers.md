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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/growthhackers-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/growthhackers-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/growthhackers-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/growthhackers-rate-limits.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/growthhackers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/growthhackershq
- group: company
  title: ''
  type: Website
  url: https://growthhackers.com/
- group: company
  title: ''
  type: Blog
  url: https://growthhackers.com/news
- group: company
  title: ''
  type: BlogRSS
  url: https://growthhackers.com/feed/
- group: operate
  title: ''
  type: Community
  url: https://growthhackers.com/community/
- group: operate
  title: ''
  type: Community
  url: https://community.growthhackers.com/
- group: other
  title: ''
  type: Resources
  url: https://growthhackers.com/resources/
- group: other
  title: ''
  type: Product
  url: https://growthhackers.com/growthos
- group: start
  title: ''
  type: Signup
  url: https://growthhackers.com/join-gh/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://growthhackers.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://growthhackers.com/privacy-policy/
- group: other
  title: ''
  type: CopyrightPolicy
  url: https://growthhackers.com/copyright-policy/
coverage:
  checked: '2026-08-13'
  detail: GrowthHackers ships end-user software only — the Growth OS platform at os.growthhackers.com and the community app at community.growthhackers.com are React SPAs on a private Supabase backend, with no developer portal, reference, spec, SDK or access-request form anywhere on the estate; the Growth OS terms of service reserve "our approved APIs" but nothing is published to approve against, and api.growthhackers.com is a dangling DNS record that Cloudflare refuses to proxy (error 1000, "DNS points to prohibited IP").
  evidence:
  - status: 403
    url: https://api.growthhackers.com/
  - status: 404
    url: https://growthhackers.com/openapi.json
  - status: 404
    url: https://os.growthhackers.com/openapi.json
  - status: 404
    url: https://os.growthhackers.com/.well-known/agent-card.json
  - status: 200
    url: https://growthhackers.com/growthos-terms-of-service/
  reason: no-developer-program
  state: none
created: '2026-03-24'
description: GrowthHackers (Growth Hackers Company, LLC) is a growth-marketing community and software company built around the growth-hacking discipline Sean Ellis named. It runs an invite-only community for founders, heads of growth, marketers and product managers, publishes growth research, case studies, opinion pieces and the State of Growth survey, and hosts webinars, AMAs and a conference. Alongside the community it sells growth and AI marketing services and ships Growth OS, an AI-powered growth and optimization platform for agencies that combines experiment planning, content creation, digital marketing execution and reporting. GrowthHackers publishes no public API, developer portal, SDK or machine-readable specification.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/growthhackers.png
layout: provider
modified: '2026-08-13'
name: GrowthHackers
nav: Providers
network: true
overview: 'GrowthHackers is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Community, Growth Hacking, Marketing, Growth Marketing, and Experimentation.


  GrowthHackers'' developer surface includes engineering blog, signup flow, and 15 more developer resources.'
plans:
- name: Growthhackers Plans Pricing
  plan_count: 0
  slug: growthhackers-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Growthhackers Rate Limits
  slug: growthhackers-rate-limits
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 7
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 13.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 25.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/growthhackers/refs/heads/main/screenshots/growthhackers-2026-06-20T182419.png
security:
- kind: domain-security
  name: Growthhackers Domain Security
  slug: growthhackers-domain-security
  summary_line: TLSv1.3 · DMARC
slug: growthhackers
tags:
- Community
- Growth Hacking
- Marketing
- Growth Marketing
- Experimentation
- Content Marketing
- Event
- Education
- Agency Services
- AI Marketing
website: https://growthhackers.com/
---
