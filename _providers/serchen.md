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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 4.7
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.serchen.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.serchen.com/get-listed
- group: start
  title: ''
  type: Login
  url: https://www.serchen.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.serchen.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.serchen.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.serchen.com/terms
- group: operate
  title: ''
  type: Contact
  url: https://www.serchen.com/contact
- group: operate
  title: ''
  type: Support
  url: https://www.serchen.com/contact
- group: company
  title: ''
  type: Newsletter
  url: https://newsletter.serchen.com/
- group: other
  title: ''
  type: X
  url: https://x.com/serchen
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/company/serchen
- group: commercial
  title: ''
  type: Plans
  url: plans/serchen-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/serchen-llms.txt
- group: other
  title: ''
  type: ContentSignal
  url: well-known/serchen-robots.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/serchen-domain-security.yml
coverage:
  checked: '2026-08-29'
  detail: 'Serchen is a software-listing marketplace with no developer surface at all: the site navigation and sitemap index carry no /developers or /api page, every OpenAPI, GraphQL, llms.txt and /.well-known/ path 404s on www.serchen.com, and robots.txt disallows /api/ because it is a Next.js internal route prefix rather than a published API.'
  evidence:
  - status: 404
    url: https://www.serchen.com/openapi.json
  - status: 404
    url: https://www.serchen.com/graphql
  - status: 404
    url: https://www.serchen.com/.well-known/api-catalog
  - status: 404
    url: https://www.serchen.com/.well-known/agent-card.json
  - status: 404
    url: https://www.serchen.com/llms.txt
  - status: 200
    url: https://www.serchen.com/sitemap.xml
  - status: 200
    url: https://www.serchen.com/robots.txt
  reason: no-developer-program
  state: none
created: '2026-03-24'
description: 'Serchen is a business-software marketplace and buyer review platform operated by Ketchell Ltd of Bournemouth, United Kingdom, trading as Serchen since 1997. It lists software products and IT service providers across hundreds of categories and industry hubs, collects and moderates first-hand buyer reviews, generates AI review summaries, and lets buyers compare products side by side. Vendors claim a free listing and can pay for Basic or Premium Membership, newsletter placement in Serchen Daily, category spotlights and guest posts. Serchen is a discovery and demand surface rather than a software vendor: it publishes no public API, SDK, webhook surface or developer portal, and its only machine-readable artifacts are a sitemap index and a robots.txt carrying Cloudflare Content-Signal directives.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/serchen.png
layout: provider
modified: '2026-08-29'
name: Serchen
nav: Providers
network: true
overview: 'Serchen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Services, Directory, Software-as-a-Service, Software Marketplace, and Reviews.


  Serchen''s developer surface includes getting-started guide, engineering blog, support, and 12 more developer resources.'
plans:
- name: Serchen Plans Pricing
  plan_count: 3
  slug: serchen-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Serchen Rate Limits
  slug: serchen-rate-limits
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 7
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 22.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/serchen/refs/heads/main/screenshots/serchen-2026-06-20T193716.png
security:
- kind: domain-security
  name: Serchen Domain Security
  slug: serchen-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: serchen
tags:
- Cloud Services
- Directory
- Software-as-a-Service
- Software Marketplace
- Reviews
- Business Software
- Vendor Discovery
- Comparison
- Lead Generation
website: https://www.serchen.com/
---
