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
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-09-25'
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
  href: https://raw.githubusercontent.com/api-evangelist/raycast/refs/heads/main/security/raycast-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/raycast/refs/heads/main/plans/raycast-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/raycast-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/raycast/refs/heads/main/rate-limits/raycast-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/raycast-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/raycast/refs/heads/main/finops/raycast-finops.yml
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
overview: 'Raycast publishes 3 APIs on the [APIs.io](https://apis.io/) network, including Extension API (SDK), AI API, and 1 more. Tagged areas include Productivity, Launcher, Extensions, SDK, and Artificial Intelligence.


  Raycast''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Raycast Plans Pricing
  plan_count: 5
  slug: raycast-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 4
  name: Raycast Rate Limits
  slug: raycast-rate-limits
score:
  band: thin
  composite: 26.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 61.6
    catalog_earned_first_party: 0.0
    catalog_gap: 53.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 36.3
    contract_governance: 0.0
    contract_quality: 25.1
    developer_ergonomics: 19.0
    discoverability: 66.1
    operational_transparency: 31.1
  previous_composite: 30.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
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
