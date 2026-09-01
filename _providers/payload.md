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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Payload is a TypeScript-first headless CMS and application framework that automatically generates REST, GraphQL, and Local APIs from collection schemas, with built-in authentication, access control, a
  name: Payload
  slug: payload
- description: The Authentication API from Payload — 8 operation(s) for authentication.
  name: Payload Authentication API
  slug: payload-authentication-api
- description: The Collections API from Payload — 3 operation(s) for collections.
  name: Payload Collections API
  slug: payload-collections-api
- description: The Globals API from Payload — 1 operation(s) for globals.
  name: Payload Globals API
  slug: payload-globals-api
- description: The Preferences API from Payload — 1 operation(s) for preferences.
  name: Payload Preferences API
  slug: payload-preferences-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Payload CMS REST Authentication API
  slug: open-payload-authentication-api
- collection_type: open
  name: Payload CMS REST Collections API
  slug: open-payload-collections-api
- collection_type: open
  name: Payload CMS REST Globals API
  slug: open-payload-globals-api
- collection_type: open
  name: Payload CMS REST Preferences API
  slug: open-payload-preferences-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/payload-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/payload-cms
- group: company
  title: ''
  type: Website
  url: https://payloadcms.com/
- group: docs
  title: ''
  type: Documentation
  url: https://payloadcms.com/docs
- group: company
  title: ''
  type: Blog
  url: https://payloadcms.com/posts
- group: build
  title: ''
  type: GitHub
  url: https://github.com/payloadcms/payload
- group: operate
  title: ''
  type: Community
  url: https://discord.com/invite/payload
- group: commercial
  title: ''
  type: Pricing
  url: https://payloadcms.com/cloud-pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://payloadcms.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://payloadcms.com/privacy
- group: agent
  title: ''
  type: LlmsText
  url: https://payloadcms.com/llms.txt
created: '2025-02-24'
description: Payload is an open-source TypeScript-first headless CMS and application framework that ships with auto-generated REST, GraphQL, and Local APIs, authentication, access control, file storage, and a Next.js-native admin UI used to build content-driven websites, applications, and digital products.
finops:
- name: Payload Finops
  service_category: API
  slug: payload-finops
graphqls:
- description: Payload is a TypeScript-first headless CMS and application framework that automatically generates REST, GraphQL, and Local APIs from collection schemas, with built-in authentication, access control, a
  name: Payload GraphQL API
  slug: payload-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/payload.png
layout: provider
modified: '2026-04-28'
name: Payload
nav: Providers
network: true
overview: 'Payload publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Collections API, Globals API, and 1 more. Tagged areas include Application Framework, CMS, Content, Headless, and Next.js.


  Payload''s developer surface includes documentation, engineering blog, GitHub presence, pricing, and 7 more developer resources.'
plans:
- name: Payload Plans Pricing
  plan_count: 3
  slug: payload-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Payload Rate Limits
  slug: payload-rate-limits
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 10
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 46.9
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 35.3
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/payload/refs/heads/main/screenshots/payload-2026-06-20T191457.png
security:
- kind: domain-security
  name: Payload Domain Security
  slug: payload-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: payload
tags:
- Application Framework
- CMS
- Content
- Headless
- Next.js
- TypeScript
website: https://payloadcms.com/
---
