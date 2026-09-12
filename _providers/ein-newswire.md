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
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ein-newswire-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/einpresswire
- group: company
  title: ''
  type: Website
  url: https://www.einpresswire.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.einpresswire.com/pricing
- group: operate
  title: ''
  type: FAQ
  url: https://www.einpresswire.com/faq
- group: operate
  title: ''
  type: Contact
  url: https://www.einpresswire.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.einpresswire.com/terms
- group: learn
  title: ''
  type: Tutorials
  url: https://www.einpresswire.com/video-tutorials
- group: other
  title: ''
  type: RSS
  url: https://www.einpresswire.com/all-rss
- group: other
  title: ''
  type: Distribution
  url: https://www.einpresswire.com/distribution-details/
- group: other
  title: ''
  type: Resources
  url: https://www.einpresswire.com/resources
- group: company
  title: ''
  type: Blog
  url: https://einpresswire.substack.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.einpresswire.com/knowledge-base
- group: start
  title: ''
  type: GettingStarted
  url: https://www.einpresswire.com/how-it-works
- group: start
  title: ''
  type: SignUp
  url: https://www.einpresswire.com/free-press-release-distribution
- group: start
  title: ''
  type: Login
  url: https://www.einpresswire.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.einpresswire.com/privacy-policy
- group: company
  title: ''
  type: About
  url: https://www.einpresswire.com/about
- group: commercial
  title: ''
  type: Plans
  url: plans/ein-newswire-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ein-newswire-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ein-newswire-llms.txt
coverage:
  checked: '2026-09-06'
  detail: EIN Presswire's own FAQ states "We only accept press release submissions through the website" and every contract-discovery probe missed, so the only API in the family is parent Newsmatics' separate News Index product on newsmatics.com — a different product line, not an EIN Presswire interface, and deliberately not recorded here.
  evidence:
  - status: 200
    url: https://www.einpresswire.com/faq
  - status: 404
    url: https://www.einpresswire.com/openapi.json
  - status: 404
    url: https://api.einpresswire.com/.well-known/agent-card.json
  - status: 404
    url: https://www.einpresswire.com/llms.txt
  reason: no-developer-program
  state: none
created: '2025-06-06'
description: 'EIN Presswire, operated by Newsmatics Inc. of Washington, D.C., is a press release distribution service for businesses, agencies, nonprofits and public figures. Releases are submitted through its web form, editorially reviewed, and syndicated to AP News, the USA TODAY Network, Nexstar Media Group, Google News, Bing, Bloomberg Terminals, MuckRack, Moody''s NewsEdge, Naviga and 3,900+ Affinity Group Publications, then published as RSS feeds broken out by industry, country and US state. Distribution is sold as prepaid packages rather than subscriptions, and there is no public developer API: the company''s own FAQ states that press releases are only accepted through the website submission form.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ein-newswire.png
layout: provider
modified: '2026-09-06'
name: EIN Newswire
nav: Providers
network: true
overview: 'EIN Newswire is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Media, News Distribution, Press Releases, Public Relations, and Newswire.


  EIN Newswire''s developer surface includes pricing, FAQ, engineering blog, documentation, getting-started guide, signup flow, and 15 more developer resources.'
plans:
- name: Ein Newswire Plans Pricing
  plan_count: 3
  slug: ein-newswire-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Ein Newswire Rate Limits
  slug: ein-newswire-rate-limits
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 50.0
    operational_transparency: 0.0
  previous_composite: 25.0
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/ein-newswire/refs/heads/main/screenshots/ein-newswire-2026-06-20T180524.png
security:
- kind: domain-security
  name: Ein Newswire Domain Security
  slug: ein-newswire-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ein-newswire
tags:
- Media
- News Distribution
- Press Releases
- Public Relations
- Newswire
- Content Syndication
- RSS
- Marketing
website: https://www.einpresswire.com/
---
