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
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/discovercloud-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/discovercloud-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/discovercloud-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/discovercloud-rate-limits.yml
- group: company
  title: ''
  type: Website
  url: https://www.discovercloud.com/
- group: company
  title: ''
  type: About
  url: https://www.discovercloud.com/about-us
- group: start
  title: ''
  type: SignUp
  url: https://www.discovercloud.com/become-a-vendor
- group: docs
  title: ''
  type: Documentation
  url: https://www.discovercloud.com/knowledge-base
- group: company
  title: ''
  type: Blog
  url: https://www.discovercloud.com/blog/
- group: operate
  title: ''
  type: Contact
  url: https://www.discovercloud.com/contact-us
- group: operate
  title: ''
  type: Support
  url: https://www.discovercloud.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.discovercloud.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.discovercloud.com/privacy-policy
- group: other
  title: ''
  type: X
  url: https://twitter.com/discover_cloud
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chekkt
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/DiscoverCloud
coverage:
  checked: '2026-09-06'
  detail: 'DiscoverCloud is a B2B software-review marketplace with no developer program of any kind: there is no api./docs./developers. subdomain (all NXDOMAIN), no GitHub organization, no package on npm, PyPI, RubyGems or crates.io, and every conventional spec and /.well-known/ path on www.discovercloud.com — /openapi.json, /swagger.json, /api-docs, /graphql, /llms.txt, /.well-known/security.txt, /.well-known/agent-card.json — is swallowed by the ASP.NET catch-all 302 to /pagenotfound; the only JSON surface on the host is the unauthenticated, undocumented ASP.NET Web API under /api/ that its own Angular front-end calls, which exposes no swagger, no /Help page and no reference.'
  evidence:
  - status: 302
    url: https://www.discovercloud.com/openapi.json
  - status: 302
    url: https://www.discovercloud.com/swagger/docs/v1
  - status: 302
    url: https://www.discovercloud.com/.well-known/agent-card.json
  - status: 302
    url: https://www.discovercloud.com/llms.txt
  - status: 404
    url: https://www.discovercloud.com/api/swagger.json
  - status: 0
    url: https://api.discovercloud.com/
  reason: no-developer-program
  state: none
created: '2026-03-24'
description: Discover the best SaaS solutions and B2B services on the DiscoverCloud. Our B2B marketplace features an ever-growing number of SaaS solutions and outsourced services. Operated by Chekkt Limited, DiscoverCloud aggregates crowd-sourced ratings and reviews across software categories including CRM, Project Management, Marketing Automation, Business Intelligence, eCommerce, Invoicing, Help Desk, and Security.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/discovercloud.png
layout: provider
modified: '2026-09-06'
name: DiscoverCloud
nav: Providers
network: true
overview: 'DiscoverCloud is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Services, Marketplace, Software-as-a-Service, Software Discovery, and Reviews.


  DiscoverCloud''s developer surface includes signup flow, documentation, engineering blog, support, and 12 more developer resources.'
plans:
- name: Discovercloud Plans Pricing
  plan_count: 0
  slug: discovercloud-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Discovercloud Rate Limits
  slug: discovercloud-rate-limits
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.9
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/discovercloud/refs/heads/main/screenshots/discovercloud-2026-06-20T180041.png
security:
- kind: domain-security
  name: Discovercloud Domain Security
  slug: discovercloud-domain-security
  summary_line: TLSv1.3
slug: discovercloud
tags:
- Cloud Services
- Marketplace
- Software-as-a-Service
- Software Discovery
- Reviews
- Business Software
website: https://www.discovercloud.com/
---
