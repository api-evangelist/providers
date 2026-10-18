---
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API reference for Curalate provided via Bazaarvoice developer portal. Documentation is HTML pages without a machine‑readable OpenAPI or other contract.
  name: Curalate API
  slug: curalate-api
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/curalate/refs/heads/main/well-known/curalate-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/curalate-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/curalate/refs/heads/main/well-known/curalate-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/curalate-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/curalate/refs/heads/main/llms/curalate-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/curalate-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/curalate/refs/heads/main/hosts/curalate-hosts.yml
  title: ''
  type: Hosts
  url: hosts/curalate-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/curalate/refs/heads/main/vendors/curalate-vendors.yml
  title: ''
  type: Vendors
  url: vendors/curalate-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.bazaarvoice.com/company/trust/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bazaarvoice.com/legal/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://support.bazaarvoice.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bazaarvoice.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bazaarvoice.com/legal/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bazaarvoice.com/pricing-and-packages/
- group: company
  title: ''
  type: Newsroom
  url: https://www.bazaarvoice.com/press/
- group: other
  title: ''
  type: Leadership
  url: https://www.bazaarvoice.com/company/leadership/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.bazaarvoice.com/
- group: company
  title: ''
  type: Blog
  url: https://www.bazaarvoice.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.curalate.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/curalate/refs/heads/main/security/curalate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/curalate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.curalate.com
coverage:
  checked: '2026-10-12'
  detail: Documentation is provided as HTML pages without an OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract.
  evidence:
  - status: 200
    url: https://developers.curalate.com/api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Curalate provides a visual commerce platform that enables brands and retailers to harness user‑generated content, shoppable photos, and influencer marketing to drive sales. After being acquired by Bazaarvoice, Curalate’s technology integrates with Bazaarvoice’s suite to deliver social commerce solutions, allowing shoppers to purchase directly from images and videos across web and mobile experiences. The platform offers analytics, content moderation, and campaign tools for marketers seeking authentic, visual-driven engagement.
image: https://media.bazaarvoice.com/Website-generic-meta-image.png
layout: provider
modified: '2026-10-12'
name: Curalate
nav: Providers
network: true
overview: 'Curalate is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Visual Commerce, Influencer Marketing, Social Shopping, Analytics, and E-Commerce.


  Curalate''s developer surface includes support, pricing, engineering blog, documentation, and 14 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 67.9
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Curalate Domain Security
  slug: curalate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: curalate
tags:
- Visual Commerce
- Influencer Marketing
- Social Shopping
- Analytics
- E-Commerce
website: https://www.curalate.com
---
