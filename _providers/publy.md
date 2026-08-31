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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://publy.co
- group: commercial
  title: ''
  type: TermsOfService
  url: https://publy.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://publy.co/policy
- group: operate
  title: ''
  type: Support
  url: https://publy.co/support/customer-service
- group: auth
  title: ''
  type: DomainSecurity
  url: security/publy-domain-security.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://publy.co/free-trial
- group: start
  title: ''
  type: SignUp
  url: https://publy.co/signup
- group: commercial
  title: ''
  type: Plans
  url: plans/publy-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/publy-llms.txt
coverage:
  checked: '2026-08-13'
  detail: PUBLY ships only a Korean consumer career-membership web/app product — publy.co returns hard 404s for /openapi.json, /graphql, /apis.json and every /.well-known/ path, api./docs./developer. subdomains do not resolve at all, and robots.txt exposes only an undocumented internal app backend (Disallow /api/**), so there is no developer program to profile.
  evidence:
  - status: 404
    url: https://publy.co/openapi.json
  - status: 404
    url: https://publy.co/.well-known/agent-card.json
  - status: 404
    url: https://publy.co/.well-known/security.txt
  - status: 200
    url: https://publy.co/robots.txt
  - status: 200
    url: https://publy.co/free-trial
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: PUBLY is a Korean career-development and content membership platform operated by NEWNEEK Co., Ltd. (뉴닉). It offers a subscription-based Career Membership giving working professionals access to curated career content, series, templates and job-transition guides, personalized daily recommendations by career stage, an AI feature (Perdy, beta), and a newsletter. It was surfaced as a portfolio company of 500 Global and added to the API Evangelist network; PUBLY publishes a consumer web product and does not expose a public developer API, so this profile carries identity and security-posture signal only.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/publy.png
layout: provider
modified: '2026-08-13'
name: PUBLY
nav: Providers
network: true
overview: 'PUBLY is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Content, Media, Career, and Membership.


  PUBLY''s developer surface includes support, pricing, signup flow, and 6 more developer resources.'
plans:
- name: Publy Plans Pricing
  plan_count: 2
  slug: publy-plans-pricing
random_paper: 10
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 5
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 19.9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Publy Domain Security
  slug: publy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: publy
tags:
- Company
- Content
- Media
- Career
- Membership
- Subscription
- Newsletter
- Professional Development
- Korea
website: https://publy.co
---
