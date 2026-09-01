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
    consent_identity: true
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
  score: 2.2
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://instaagent.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://instaagent.com/terms-and-condition
- group: other
  title: ''
  type: ContentSignal
  url: well-known/instaagent-robots.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/instaagent-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/instaagent-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/instaagent-plans-pricing.yml
- group: operate
  title: ''
  type: Contact
  url: https://instaagent.com/#contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/112974856/
- group: other
  title: ''
  type: X
  url: https://x.com/InstaAgentAI
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/instaagent.ai
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/profile.php?id=61575219352924
coverage:
  checked: '2026-08-12'
  detail: 'InstaAgent ships only an end-user marketing product: instaagent.com is a three-URL Next.js site whose sitemap lists just /, /zh and /terms-and-condition, no api./docs./developer./app. subdomain resolves in DNS, there is no GitHub organization, and the sole conversion path is a "Request Demo" CTA with a mailto to kyle@instaagent.com.'
  evidence:
  - status: 200
    url: https://instaagent.com/
  - status: 404
    url: https://instaagent.com/openapi.json
  - status: 404
    url: https://instaagent.com/docs
  - status: 404
    url: https://instaagent.com/developers
  - status: 404
    url: https://instaagent.com/.well-known/agent-card.json
  - status: 404
    url: https://instaagent.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/instaagent
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: InstaAgent is a Y Combinator-backed AI marketing platform that turns a single campaign brief into hundreds of audience-specific creatives. It generates persona-, trend-, and format-grounded ad variants, distributes them across Meta, TikTok, and niche social accounts built for specific audiences, then tests which personas, hooks, formats, and channels drive performance and scales the winners into the next campaign. The company reports serving 500+ clients across 10+ countries with 10x ad variants and 30%+ ROI improvement. InstaAgent operates a marketing product surface only and does not currently publish a public developer API, SDKs, or developer documentation; this profile captures its public identity and domain-security posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/instaagent.png
layout: provider
modified: '2026-08-12'
name: InstaAgent
nav: Providers
network: true
overview: InstaAgent is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Advertising, Artificial Intelligence, and Social-Media.
plans:
- name: Instaagent Plans Pricing
  plan_count: 0
  slug: instaagent-plans-pricing
random_paper: 20
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/instaagent/refs/heads/main/screenshots/instaagent-2026-07-25T222557.png
security:
- kind: domain-security
  name: Instaagent Domain Security
  slug: instaagent-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: instaagent
tags:
- Company
- Marketing
- Advertising
- Artificial Intelligence
- Social-Media
- Campaigns
- Content Generation
- Y Combinator
website: https://instaagent.com/
---
