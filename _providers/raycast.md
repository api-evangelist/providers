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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://developers.raycast.com
  baseurl_source: spec
  description: The primary developer interface - the @raycast/api npm package. A strongly typed TypeScript/Node SDK (installed via `npm i @raycast/api`) providing React UI components (List, Detail, Form, Grid, Actio
  name: Raycast Extension API (SDK)
  slug: raycast-extension-api-sdk
- baseURL: https://developers.raycast.com
  baseurl_source: spec
  description: AI access surfaced through the SDK via `AI.ask(prompt)` - no API keys or HTTP endpoint required. Routes prompts across 80+ models from OpenAI, Anthropic, Google, Mistral, Groq, Perplexity, and xAI beh
  name: Raycast AI API
  slug: raycast-ai-api
- description: The Raycast Store distributes community and partner extensions. Publishing is done via the `ray` CLI and a pull request to the github.com/raycast/extensions monorepo; there is no documented public RES
  name: Raycast Store
  slug: raycast-store
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Raycast Extension API (SDK)
  slug: open-raycast
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/raycast-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/raycast
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/raycast
- group: company
  title: ''
  type: Website
  url: https://www.raycast.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.raycast.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/raycast-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/raycast-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/raycast-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.raycast.com/blog
created: '2026-06-20'
description: Raycast is a macOS (and Windows, in beta) productivity launcher that ships an extensions platform, built-in AI, and a Store. Its developer surface is the @raycast/api TypeScript/Node SDK used to build extensions with React - a client-side library, not a public HTTP REST API. Capabilities such as AI, Storage, OAuth, and Preferences are exposed as SDK modules invoked from inside extensions rather than as standalone web endpoints.
finops:
- name: Raycast Finops
  service_category: Productivity and Collaboration
  slug: raycast-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/raycast.png
layout: provider
modified: '2026-06-20'
name: Raycast
nav: Providers
network: true
overview: 'Raycast publishes 2 APIs on the [APIs.io](https://apis.io/) network: Extension API (SDK) and AI API. Tagged areas include Productivity, Launcher, Extensions, SDK, and Artificial Intelligence.


  Raycast''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Raycast Plans Pricing
  plan_count: 5
  slug: raycast-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 4
  name: Raycast Rate Limits
  slug: raycast-rate-limits
score:
  band: thin
  composite: 30.0
  coverage:
    artifact_dirs: 8
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 27.9
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 30.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/raycast/refs/heads/main/screenshots/raycast-2026-06-20T192715.png
security:
- kind: domain-security
  name: Raycast Domain Security
  slug: raycast-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: raycast
tags:
- Productivity
- Launcher
- Extensions
- SDK
- Artificial Intelligence
- macOS
website: https://www.raycast.com
---
