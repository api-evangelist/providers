---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: A lightweight (3kB gzipped) JavaScript SDK that lets developers programmatically create, open, and embed StackBlitz projects in web pages, documentation sites, or blog posts. Provides six primary meth
  name: StackBlitz JavaScript SDK
  slug: javascript-sdk
- description: A browser-based runtime API that executes Node.js applications and operating system commands directly inside a browser tab using WebAssembly. Provides classes and methods for booting a container insta
  name: WebContainer API
  slug: webcontainer-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stackblitz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stackblitz.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.stackblitz.com
- group: docs
  title: ''
  type: WebContainersDocumentation
  url: https://webcontainers.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stackblitz
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stackblitz
- group: company
  title: ''
  type: Blog
  url: https://blog.stackblitz.com
- group: commercial
  title: ''
  type: Pricing
  url: https://stackblitz.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.stackblitz.com
- group: other
  title: ''
  type: X
  url: https://x.com/stackblitz
- group: commercial
  title: ''
  type: Plans
  url: plans/stackblitz-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stackblitz-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/stackblitz-finops.yml
created: '2026-06-12'
description: StackBlitz is an online development environment that runs Node.js applications entirely in the browser using WebContainers, a WebAssembly-based operating system that boots Node.js in milliseconds without a remote server. It serves developers, technical writers, and platform teams who need interactive coding environments, documentation playgrounds, or embedded IDE experiences. The platform provides a JavaScript SDK for programmatically creating and embedding projects, and a WebContainer API for booting full Node.js runtimes directly inside web applications. StackBlitz also offers Codeflow, a one-click GitHub integration for pull request review and issue fixing workflows.
finops:
- name: Stackblitz Finops
  service_category: Developer Tools
  slug: stackblitz-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stackblitz.png
jsonld:
- class_count: 0
  name: Stackblitz Context
  property_count: 32
  slug: stackblitz-context
layout: provider
modified: '2026-06-12'
name: StackBlitz
nav: Providers
network: true
overview: 'StackBlitz publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Developer Tools, WebAssembly, Node.js, IDE, and Browser Runtime.


  The StackBlitz catalog on APIs.io includes 1 JSON-LD context.


  StackBlitz''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Stackblitz Plans Pricing
  plan_count: 4
  slug: stackblitz-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Stackblitz Rate Limits
  slug: stackblitz-rate-limits
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 7
    catalog_gap: 52.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 28.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stackblitz/refs/heads/main/screenshots/stackblitz-2026-06-20T194443.png
security:
- kind: domain-security
  name: Stackblitz Domain Security
  slug: stackblitz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stackblitz
tags:
- Developer Tools
- WebAssembly
- Node.js
- IDE
- Browser Runtime
- Code Environments
website: https://stackblitz.com
---
