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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: REST and GraphQL APIs for fetching, syncing, and managing content from Agility CMS, with CDN delivery across global and regional endpoints.
  name: Agility CMS API
  slug: api
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/agility-cms-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/agility-cms-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agility-cms-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agilitycms.com/
- group: docs
  title: ''
  type: Documentation
  url: https://agilitycms.com/docs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agilitycms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agility
- group: commercial
  title: ''
  type: Pricing
  url: https://agilitycms.com/product/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/agility-cms-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agility-cms-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/agility-cms-finops.md
- group: company
  title: ''
  type: Blog
  url: https://agilitycms.com/blog
created: 2026-06-14
description: Headless CMS with a GraphQL content API, page management, multi-site support, and integration SDKs for Next.js, Gatsby, Nuxt, and other frameworks.
graphqls:
- description: 'Source: https://agilitycms.com/docs/developers/graphql-api'
  name: Agility CMS GraphQL API
  slug: agility-cms-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agility-cms.png
layout: provider
modified: 2026-06-14
name: Agility CMS
nav: Providers
network: true
overview: 'Agility CMS publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, Headless CMS, Content Management, REST, and Multi-Site.


  Agility CMS''s developer surface includes documentation, pricing, engineering blog, and 9 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 23.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 41.5
    developer_ergonomics: 11.9
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 23.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agility-cms/refs/heads/main/screenshots/agility-cms-2026-06-20T170242.png
security:
- kind: domain-security
  name: Agility Cms Domain Security
  slug: agility-cms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Agility Cms Vulnerability Disclosure
  slug: agility-cms-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Agility Cms Trust Center
  slug: agility-cms-trust-center
  summary_line: SOC 2, GDPR
slug: agility-cms
tags:
- GraphQL
- Headless CMS
- Content Management
- REST
- Multi-Site
website: https://agilitycms.com/
---
