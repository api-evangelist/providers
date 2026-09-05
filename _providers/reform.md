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
    error_semantics: false
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
  score: 22.3
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Reform's public integration surface. It is not a REST management API — no endpoint exists to create, read or update forms and submissions. What Reform publishes is the hosted form host (forms.reform.a
  name: Reform Forms
  slug: reform-forms
artifact_total: 9
asyncapis:
- description: ''
  name: Reform Webhooks
  slug: reform-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reform-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.reform.app/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.reform.app/
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.reform.app/
- group: operate
  title: ''
  type: Support
  url: https://docs.reform.app/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.reform.app/article/49-building-your-first-form
- group: company
  title: ''
  type: Blog
  url: https://www.reform.app/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.reform.app/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.reform.app/register
- group: start
  title: ''
  type: Login
  url: https://dashboard.reform.app/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.reform.app/legal/terms-of-service
- group: other
  title: ''
  type: Templates
  url: https://www.reform.app/templates
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/reformapp
- group: other
  title: ''
  type: X
  url: https://x.com/heyreform
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/reform-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/reform-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/reform-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/reform-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/reform-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reform-authentication.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/reform-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/reform-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/reform-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/reform-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/reform-trust-center.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/reform/refs/heads/main/plans/reform-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/reform/refs/heads/main/rate-limits/reform-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/reform/refs/heads/main/finops/reform-finops.yml
created: '2026-06-13'
description: Reform is a conversion-focused, no-code form builder for B2B and SaaS teams, acquired by conversion-rate-optimization agency FunnelEnvy. It builds multi-step forms with conditional logic, lead qualification and enrichment, and syncs submissions to CRMs and marketing platforms. Reform publishes no REST API, SDK or OpenAPI definition; its integration surface is three published pieces — a signed outbound webhook (form.submitted, HMAC-SHA256), a CDN-hosted browser embed loader with a parent-page event API, and a headless mode that posts your own HTML form to Reform using answers[block-id] field naming.
finops:
- name: Reform Finops
  service_category: ''
  slug: reform-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reform.png
jsonld:
- class_count: 16
  name: Reform Context
  property_count: 1
  slug: reform-context
layout: provider
modified: '2026-08-14'
name: Reform
nav: Providers
network: true
overview: 'Reform publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Forms, Form Builder, Lead Generation, Headless Forms, and Webhook.


  The Reform catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Reform''s developer surface includes documentation, support, getting-started guide, engineering blog, pricing, signup flow, authentication, and 21 more developer resources.'
plans:
- name: Reform Plans Pricing
  plan_count: 4
  slug: reform-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Reform Rate Limits
  slug: reform-rate-limits
score:
  band: developing
  composite: 49.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 60.0
    catalog_earned_first_party: 12.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 89.5
    commercial_clarity: 89.5
    contract_governance: 18.2
    contract_quality: 51.9
    developer_ergonomics: 40.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 49.8
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reform/refs/heads/main/screenshots/reform-2026-06-20T192748.png
security:
- kind: authentication
  name: Reform Authentication
  slug: reform-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Reform Domain Security
  slug: reform-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Reform Trust Center
  slug: reform-trust-center
  summary_line: SOC 2, ISO 27001
slug: reform
tags:
- Forms
- Form Builder
- Lead Generation
- Headless Forms
- Webhook
- No-Code
- Integration
- CRM
- Conversion Rate Optimization
- Embeddable Components
website: https://www.reform.app/
---
