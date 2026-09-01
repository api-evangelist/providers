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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Defer platform exposes a TypeScript SDK for declaring deferred functions and a managed control plane that schedules, queues, retries, and observes their execution. Functions are defined with decor
  name: Defer Platform
  slug: defer-platform
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/defer-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/defer-inc
- group: company
  title: ''
  type: Website
  url: https://www.defer.run
- group: docs
  title: ''
  type: Documentation
  url: https://docs.defer.run
- group: build
  title: ''
  type: GitHub
  url: https://github.com/defer-run
created: '2026-03-27'
description: Defer was a TypeScript-first background job and workflow automation platform for Node.js applications that let developers schedule, queue, and orchestrate serverless functions with built-in retries, throttling, concurrency controls, and scheduled (CRON) execution. Defer integrated with frameworks such as Next.js, Remix, and SvelteKit through an SDK and a managed control plane. The defer.run service has since transitioned and the defer.run domain currently redirects to digger.tools; this entry preserves the historical profile and links to the surviving documentation, GitHub organization, and references.
finops:
- name: Defer Finops
  service_category: API
  slug: defer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/defer.png
layout: provider
modified: '2026-04-28'
name: Defer
nav: Providers
network: true
overview: 'Defer publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Background Jobs, Cron, Developer-First, Node.js, and Queues.


  Defer''s developer surface includes documentation, GitHub presence, and 3 more developer resources.'
plans:
- name: Defer Plans Pricing
  plan_count: 3
  slug: defer-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Defer Rate Limits
  slug: defer-rate-limits
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 5
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Defer Domain Security
  slug: defer-domain-security
  summary_line: TLSv1.3
slug: defer
tags:
- Background Jobs
- Cron
- Developer-First
- Node.js
- Queues
- Scheduling
- Serverless
- TypeScript
- Workflow-Automation
website: https://www.defer.run
---
