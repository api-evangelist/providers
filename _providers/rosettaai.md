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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rosettaai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rosetta.ai
- group: docs
  title: ''
  type: Documentation
  url: https://rosetta-ai.gitbook.io/help-center/
- group: start
  title: ''
  type: GettingStarted
  url: https://rosetta-ai.gitbook.io/help-center/onboarding/getting-started
- group: operate
  title: ''
  type: Support
  url: https://rosetta-ai.gitbook.io/help-center/support/faq
- group: company
  title: ''
  type: Blog
  url: https://rosetta.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://rosetta.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.rosetta.ai/register
- group: start
  title: ''
  type: Login
  url: https://dashboard.rosetta.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rosetta.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rosetta.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rosetta-ai
- group: operate
  title: ''
  type: ChangeLog
  url: https://rosetta-ai.gitbook.io/help-center/support/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rosettaai-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rosettaai-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/rosettaai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rosettaai-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/rosettaai-packages.yml
- group: design
  title: ''
  type: Components
  url: components/rosettaai-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rosettaai-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rosettaai-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rosettaai-lifecycle.yml
created: '2026-07-17'
description: Rosetta.ai is a Taipei-based e-commerce personalization and marketing automation platform that uses AI, image recognition, and deep learning to tailor the online shopping experience for every visitor. Its product suite spans Rosetta Engage (AI product recommenders), Rosetta AdMatch (personalized advertising and traffic acquisition), Rosetta Analytics (machine-learning consumer and product insight), and Rosetta Automation (multi-channel EDM, SMS, and LINE marketing). The platform is delivered as a hosted SaaS dashboard and as a Shopify app ("Personalization Upsell Dealer"), integrating with storefronts through Google Tag Manager and product-feed connections rather than a public developer REST API. A first-party REST API does run at api.rosetta.ai — the production tag authenticates to it with a Bearer token and an application/vnd.rosetta-ai.v2+json media type — but Rosetta.ai publishes no reference, no specification and no developer program for it, so it is an internal contract
  rather than a product. This profile was surfaced as a 500 Global portfolio company and enriched from Rosetta.ai's public marketing site, GitBook help center, CDN distribution, and GitHub organization.
image: https://images.prismic.io/rosetta-marketing-website/9621daef-3ce6-47d3-abec-1a4210f8fbb9_Social%20Card%20-%20Homepage.png
layout: provider
modified: '2026-08-13'
name: Rosetta.ai
nav: Providers
network: true
overview: 'Rosetta.ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Personalization, Recommendations, and Marketing Automation.


  Rosetta.ai''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, changelog, and 15 more developer resources.'
plans:
- name: Rosettaai Plans Pricing
  plan_count: 3
  slug: rosettaai-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Rosettaai Rate Limits
  slug: rosettaai-rate-limits
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 24.8
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rosettaai/refs/heads/main/screenshots/rosettaai-2026-09-02T154130.png
security:
- kind: authentication
  name: Rosettaai Authentication
  slug: rosettaai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Rosettaai Domain Security
  slug: rosettaai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rosettaai
tags:
- Company
- E-Commerce
- Personalization
- Recommendations
- Marketing Automation
- Artificial Intelligence
- Retail
- Shopify
- Machine-Learning
- Conversion Optimization
website: https://rosetta.ai
---
