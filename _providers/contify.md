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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The Contify News API is a developer-friendly REST/JSON API that aggregates, deduplicates, and enriches business news from over a million curated sources, covering 700,000+ companies and 117+ languages
  name: Contify News API
  slug: news-api
artifact_total: 7
asyncapis:
- description: ''
  name: Contify Webhooks
  slug: contify-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/contify-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/contifyhub
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/contify
- group: company
  title: ''
  type: Website
  url: https://www.contify.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.contify.com/news-api/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.contify.com/
- group: company
  title: ''
  type: Blog
  url: https://www.contify.com/resources/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.contify.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.contify.com/terms-conditions/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.contify.com/contact-us/
- group: auth
  title: ''
  type: Authentication
  url: authentication/contify-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/contify-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/contify-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/contify-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/contify-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/contify-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.contify.com/news-api/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/contify-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/contify-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://www.contify.com/contact-us/
- group: start
  title: ''
  type: SignUp
  url: https://www.contify.com/news-api-early-access/
- group: start
  title: ''
  type: Login
  url: https://app.contify.com/accounts/site-login/
created: '2025-02-09'
description: Contify is an AI-powered market and competitive intelligence platform that helps businesses track competitor activity, market trends, and industry news. It exposes a REST News API that delivers structured, deduplicated, and enriched business news data on companies, industries, and topics.
finops:
- name: Contify Finops
  service_category: API
  slug: contify-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/contify.png
layout: provider
modified: '2026-09-05'
name: Contify
nav: Providers
network: true
overview: 'Contify publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Competitive Intelligence, Market Intelligence, Business News, News, and Artificial Intelligence.


  The Contify catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Contify''s developer surface includes documentation, engineering blog, authentication, changelog, support, signup flow, and 16 more developer resources.'
plans:
- name: Contify Plans Pricing
  plan_count: 0
  slug: contify-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Contify Rate Limits
  slug: contify-rate-limits
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 20.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 31.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 17.1
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/contify/refs/heads/main/screenshots/contify-2026-06-20T174939.png
security:
- kind: authentication
  name: Contify Authentication
  slug: contify-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Contify Domain Security
  slug: contify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: contify
tags:
- Competitive Intelligence
- Market Intelligence
- Business News
- News
- Artificial Intelligence
- Data
- Strategies
website: https://www.contify.com/
---
