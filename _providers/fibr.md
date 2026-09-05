---
access_model:
  confidence: high
  label: Contact sales
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - https://fibr.ai/pricing
  - https://fibr.ai/book-a-demo
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://fibr.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://support.fibr.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://fibr.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://fibr.ai/blog
- group: start
  title: ''
  type: SignUp
  url: https://fibr.ai/book-a-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fibr.ai/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fibr.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://support.fibr.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getfibr-co
- group: start
  title: ''
  type: GettingStarted
  url: https://support.fibr.ai/get-started-with-fibr-ai
- group: start
  title: ''
  type: Login
  url: https://app.getfibr.co
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.fibr.ai/product-change-logs
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fibr-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/fibr-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/fibr-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fibr-lifecycle.yml
- group: other
  title: ''
  type: ContentSignal
  url: well-known/fibr-content-signals.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fibr-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fibr-support-llms.txt
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.fibr.ai/
- group: design
  title: ''
  type: Conformance
  url: conformance/fibr-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.fibr.ai/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fibr-domain-security.yml
coverage:
  checked: '2026-08-13'
  detail: Fibr ships its platform only as an end-user product — the entire developer surface is one per-workspace JavaScript tag retrieved from the authenticated dashboard, and the GitBook documentation index (support.fibr.ai/llms.txt, 200) lists no API, webhook or SDK section at all.
  evidence:
  - status: 200
    url: https://support.fibr.ai/llms.txt
  - status: 404
    url: https://fibr.ai/openapi.json
  - status: 404
    url: https://app.getfibr.co/openapi.json
  - status: 404
    url: https://fibr.ai/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/getfibr-co/repos
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Fibr AI is an Agentic Web Experience Platform that turns static URLs into intelligent, adaptive landing pages that sense visitor intent and reshape themselves in real time using AI agents with human oversight. Its core product, Fibr Web Pilot, combines no-code A/B testing, conversion-rate optimization (CRO), and personalization — including ad-to-landing-page matching, audience and LLM-visitor personalization, bulk page creation, and AI-driven experimentation — for enterprises, agencies, and growth marketers. The platform integrates with Google Ads, Meta Ads, GA4, CDPs, and major CMS tools, and also ships a large library of free AI marketing tools (headline, hook, CTA, caption, and copy generators, a CRO audit, a landing-page analyzer, and an LLMs.txt generator). Founded in 2022-2023 by Ankur "AJ" Goyal and Pritam Roy and backed by Accel, Fibr is offered through Starter, Agency, and Enterprise pricing tiers. Fibr does not currently publish a public developer API or OpenAPI; this
  profile captures its identity, developer-adjacent surface, and security/compliance posture.
image: https://framerusercontent.com/assets/XfCvovYMluHkUPTs7owlGe1ohNQ.png
layout: provider
modified: '2026-08-13'
name: Fibr
nav: Providers
network: true
overview: 'Fibr is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Conversion Rate Optimization, Personalization, Landing Pages, and A/B Testing.


  Fibr''s developer surface includes documentation, pricing, engineering blog, signup flow, support, getting-started guide, changelog, and 16 more developer resources.'
plans:
- name: Fibr Plans Pricing
  plan_count: 3
  slug: fibr-plans-pricing
random_paper: 20
score:
  band: thin
  composite: 34.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 34.5
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fibr/refs/heads/main/screenshots/fibr-2026-07-25T214410.png
security:
- kind: domain-security
  name: Fibr Domain Security
  slug: fibr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Fibr Trust Center
  slug: fibr-trust-center
  summary_line: SOC 2, ISO 27001
slug: fibr
tags:
- Company
- Conversion Rate Optimization
- Personalization
- Landing Pages
- A/B Testing
- Experimentation
- Marketing
- Artificial Intelligence
- Agentic Web
- Web Experience
website: https://fibr.ai/
---
