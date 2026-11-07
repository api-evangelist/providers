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
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/appyai/plans/appyai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/appyai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/appyai/changelog/appyai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/appyai-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.appy.ai/
- group: design
  href: https://artifacts.apis.io/appyai/conformance/appyai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/appyai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/appyai/llms/appyai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appyai-llms.txt
- group: other
  href: https://artifacts.apis.io/appyai/a2a/appyai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/appyai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/appyai/well-known/appyai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/appyai-well-known.yml
- group: other
  href: https://artifacts.apis.io/appyai/hosts/appyai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appyai-hosts.yml
- group: other
  href: https://artifacts.apis.io/appyai/vendors/appyai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appyai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appy.ai/platform/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appy.ai/platform/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://appy.ai/company/pricing
- group: start
  title: ''
  type: Login
  url: https://builder.appy.ai/signin
- group: operate
  title: ''
  type: ChangeLog
  url: https://appy.ai/changelog
- group: company
  title: ''
  type: Blog
  url: https://appy.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.appy.ai/your-ai-team/installation
- group: docs
  title: ''
  type: Documentation
  url: https://help.appy.ai/
- group: auth
  href: https://artifacts.apis.io/appyai/security/appyai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/appyai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/appyai/security/appyai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appyai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appy.ai/
coverage:
  checked: '2026-10-29'
  detail: The provider's site returns 404 for /docs and no OpenAPI or other contract was discoverable.
  evidence:
  - status: 404
    url: https://appyai.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Appyai provides AI-driven analytics and automation solutions for businesses, enabling data-driven decision making through advanced machine learning models, real-time insights, and customizable dashboards. Founded by a collective of experienced entrepreneurs, the company focuses on delivering scalable, secure, and easy-to-integrate APIs that empower developers to embed intelligent features into their applications. Backed by founder-collective, Appyai aims to accelerate digital transformation across industries.
image: https://appy.ai/og-image.png
layout: provider
modified: '2026-10-29'
name: Appyai
nav: Providers
network: true
overview: 'Appyai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Analytics, Automation, and Machine Learning.


  Appyai''s developer surface includes changelog, pricing, engineering blog, getting-started guide, documentation, and 15 more developer resources.'
plans:
- name: Appyai Plans Pricing
  plan_count: 14
  slug: appyai-plans-pricing
random_paper: 20
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.4
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 55.4
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 34.8
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/appyai/appyai-2026-11-03T121040.png
security:
- kind: domain-security
  name: Appyai Domain Security
  slug: appyai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Appyai Trust Center
  slug: appyai-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: appyai
tags:
- Company
- Artificial Intelligence
- Analytics
- Automation
- Machine Learning
website: https://appy.ai/
---
