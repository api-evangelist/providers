---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://retainiq.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://retainiq.io/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://retainiq.io/terms-and-conditions
- group: company
  title: ''
  type: Blog
  url: https://retainiq20.substack.com/
- group: operate
  title: ''
  type: Support
  url: mailto:hello@retainiq.io
- group: auth
  title: ''
  type: DomainSecurity
  url: security/retainiq-domain-security.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://retainiq.io/services
- group: commercial
  title: ''
  type: Plans
  url: plans/retainiq-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/retainiq-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/retainiq-llms.txt
- group: other
  title: ''
  type: AppStore
  url: https://apps.shopify.com/retainiq
- group: company
  title: ''
  type: Newsletter
  url: https://retainiq.io/resources
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/retainiq/
coverage:
  checked: '2026-08-13'
  detail: RetainIQ sells a managed retention-marketing service, not software with an interface — every contract and /.well-known/ path on retainiq.io returns a real 404, its former self-serve Shopify app host app.retainiq.io returns Cloudflare 522, and the developer website that app listing names (wyde.ai) now redirects to a domain-for-sale page.
  evidence:
  - status: 404
    url: https://retainiq.io/openapi.json
  - status: 404
    url: https://retainiq.io/.well-known/agent-card.json
  - status: 404
    url: https://retainiq.io/llms.txt
  - status: 522
    url: https://app.retainiq.io/
  - status: 302
    url: https://www.wyde.ai/
  - status: 200
    url: https://apps.shopify.com/retainiq
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: RetainIQ is a full-service retention-marketing agency for direct-to-consumer (D2C) brands, delivering lifecycle email and SMS programs. Its work spans automated flows (welcome, cart abandonment, post-purchase, win-back, replenishment), weekly strategic campaign sends with design and copywriting, and deliverability/segmentation/list-hygiene infrastructure. A proprietary 1:1 personalization engine generates variant product blocks at scale. A Klaviyo Gold Master Partner and Omnisend partner, RetainIQ integrates with Shopify, Klaviyo, and Omnisend; plans start at $990/mo on month-to-month terms. It operates as a marketing-services agency and does not publish a public developer API, SDK, or documentation surface. RetainIQ Global Inc. previously shipped a self-serve Shopify app (listed 2021, free to install, $999 per 100K personalization credits); that listing is still live but appears retired in place — its application host returns a Cloudflare 522 and the developer website named
  on the listing now redirects to a domain-for-sale page.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/retainiq.png
layout: provider
modified: '2026-08-13'
name: RetainIQ
nav: Providers
network: true
overview: 'RetainIQ is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Retention Marketing, Email Marketing, and SMS.


  RetainIQ''s developer surface includes engineering blog, support, pricing, and 10 more developer resources.'
plans:
- name: Retainiq Plans Pricing
  plan_count: 2
  slug: retainiq-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 19.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/retainiq/refs/heads/main/screenshots/retainiq-2026-09-02T153628.png
security:
- kind: domain-security
  name: Retainiq Domain Security
  slug: retainiq-domain-security
  summary_line: TLSv1.2 · DMARC
slug: retainiq
tags:
- Company
- Artificial Intelligence
- Retention Marketing
- Email Marketing
- SMS
- E-Commerce
- Personalization
- D2C
- Klaviyo
website: https://retainiq.io/
---
