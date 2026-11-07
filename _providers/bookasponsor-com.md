---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/bookasponsor-com/plans/bookasponsor-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bookasponsor-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/bookasponsor-com/llms/bookasponsor-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bookasponsor-com-llms.txt
- group: other
  href: https://artifacts.apis.io/bookasponsor-com/hosts/bookasponsor-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bookasponsor-com-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://bookasponsor.com/sponsors/vanta.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bookasponsor.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bookasponsor.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://bookasponsor.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://bookasponsor.com/sponsors/niche/media
- group: start
  title: ''
  type: Login
  url: https://bookasponsor.com/login
- group: auth
  href: https://artifacts.apis.io/bookasponsor-com/security/bookasponsor-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bookasponsor-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bookasponsor.com/
coverage:
  checked: '2026-11-02'
  detail: No public API documentation or machine‑readable contract was found on the provider’s site.
  evidence:
  - status: 200
    url: https://bookasponsor.com/
  reason: no-developer-program
  state: none
created: '2026-11-02'
description: Book a Sponsor helps newsletter, podcast, and YouTube creators find brands willing to sponsor their content. Users paste a link to their media, and the service scans recent sponsorships to match relevant brands, then emails those brands on the user’s behalf. The platform offers a free tier with 200 emails and paid plans starting at $19 per month, with no commission on deals. It aims to simplify sponsorship acquisition for creators and provides tools like media kits, pricing calculators, and proposal templates.
image: https://bookasponsor.com/assets/og/video-poster.jpg
layout: provider
modified: '2026-11-02'
name: Book a Sponsor
nav: Providers
network: true
overview: 'Book a Sponsor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sponsorship, Newsletters, Marketing, and Software-as-a-Service.


  Book a Sponsor''s developer surface includes pricing and 10 more developer resources.'
plans:
- name: Bookasponsor Com Plans Pricing
  plan_count: 3
  slug: bookasponsor-com-plans-pricing
random_paper: 20
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bookasponsor Com Domain Security
  slug: bookasponsor-com-domain-security
  summary_line: TLSv1.3
slug: bookasponsor-com
tags:
- Company
- Sponsorship
- Newsletters
- Marketing
- Software-as-a-Service
website: https://bookasponsor.com/
---
