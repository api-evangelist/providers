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
api_count: 6
apis:
- description: Node.js is a JavaScript runtime built on Chrome's V8 engine that powers server-side applications and tooling across the JavaScript ecosystem.
  name: Node.js
  slug: nodejs
- description: Fastify is a fast, low-overhead web framework for Node.js with a strong plugin architecture and built-in JSON Schema validation.
  name: Fastify
  slug: fastify
- description: LoopBack is a highly extensible Node.js and TypeScript framework for building APIs and microservices with built-in OpenAPI support.
  name: LoopBack
  slug: loopback
- description: Electron is a framework for building cross-platform desktop applications with web technologies (Chromium and Node.js).
  name: Electron
  slug: electron
- description: Appium is an open source automation framework for native, hybrid, and mobile web applications, exposing a WebDriver-compatible HTTP API.
  name: Appium
  slug: appium
- description: Express is a fast, unopinionated, minimalist web framework for Node.js used for building HTTP APIs and web applications.
  name: Express
  slug: express
artifact_total: 11
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/nodejs/node/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/nodejs/node/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/nodejs/node/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/nodejs/node/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/nodejs/node/blob/main/CONTRIBUTING.md
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/openjs-foundation-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openjs-foundation-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openjs-foundation
- group: company
  title: ''
  type: Website
  url: https://openjsf.org/
- group: docs
  title: ''
  type: Documentation
  url: https://openjsf.org/projects
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/openjs-foundation
- group: company
  title: ''
  type: Blog
  url: https://openjsf.org/blog/
created: '2026-03-16'
description: The OpenJS Foundation is a Linux Foundation project that supports the growth of JavaScript and web technologies through open governance and collaboration. It hosts critical web ecosystem projects including Node.js, jQuery, Electron, webpack, ESLint, Express, Fastify, LoopBack, Appium, Mocha, Jest, and many more.
finops:
- name: Openjs Foundation Finops
  service_category: API
  slug: openjs-foundation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openjs-foundation.png
layout: provider
modified: '2026-07-25'
name: OpenJS Foundation
nav: Providers
network: true
overview: 'OpenJS Foundation publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include JavaScript, Linux Foundation, Node.js, Web, and API Frameworks.


  OpenJS Foundation''s developer surface includes documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Openjs Foundation Plans Pricing
  plan_count: 3
  slug: openjs-foundation-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Openjs Foundation Rate Limits
  slug: openjs-foundation-rate-limits
score:
  band: emerging
  composite: 25.4
  coverage:
    artifact_dirs: 6
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 39.5
  open_source:
    applies: true
    score: 100.0
  previous_composite: 25.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openjs-foundation/refs/heads/main/screenshots/openjs-foundation-2026-06-20T191008.png
security:
- kind: domain-security
  name: Openjs Foundation Domain Security
  slug: openjs-foundation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Openjs Foundation Vulnerability Disclosure
  slug: openjs-foundation-vulnerability-disclosure
  summary_line: disclosure policy published
slug: openjs-foundation
tags:
- JavaScript
- Linux Foundation
- Node.js
- Web
- API Frameworks
website: https://openjsf.org/
---
