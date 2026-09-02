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
api_count: 2
apis:
- description: Storybook is an open-source frontend workshop for building UI components and pages in isolation. Supports React, Vue, Angular, Svelte, Web Components, Ember, Preact, and more. Core features include co
  name: Storybook
  slug: storybook
- description: 'The Storybook MCP (Model Context Protocol) server enables AI agents to interact with a running Storybook instance. Available as the @storybook/addon-mcp addon (runs within the dev server at /mcp) and '
  name: Storybook MCP Server
  slug: storybook-mcp
artifact_total: 13
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/storybookjs/storybook/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/storybookjs/storybook/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/storybookjs/storybook/blob/next/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/storybookjs/storybook/blob/next/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/storybookjs/storybook/blob/next/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/storybookjs/storybook/blob/next/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/storybook-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://storybook.js.org/
- group: docs
  title: ''
  type: Documentation
  url: https://storybook.js.org/docs
- group: company
  title: ''
  type: Blog
  url: https://storybook.js.org/blog
- group: learn
  title: ''
  type: Tutorials
  url: https://storybook.js.org/tutorials/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://storybook.js.org/releases
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/storybookjs
- group: build
  title: ''
  type: NPM
  url: https://www.npmjs.com/package/storybook
- group: other
  title: ''
  type: X
  url: https://x.com/storybookjs
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/storybook
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@chromaticui
created: '2025-01-08'
description: Storybook is the industry-standard frontend workshop for building, documenting, and testing UI components in isolation. It supports React, Vue, Angular, Svelte, Web Components, and a dozen other frameworks. Developers write stories capturing component states, use addons for interaction testing, accessibility auditing, visual testing, and design integration, and publish component documentation for design systems and component libraries. Storybook 10+ includes an MCP server enabling AI agents to understand components, generate stories, and run tests. The project is open source (MIT) and maintained by the storybookjs GitHub organization.
examples:
- key_count: 3
  name: Storybook Button Story Example
  slug: storybook-button-story-example
- key_count: 5
  name: Storybook Mcp List Documentation Example
  slug: storybook-mcp-list-documentation-example
finops:
- name: Storybook Finops
  service_category: API
  slug: storybook-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/storybook.png
json_schemas:
- name: Storybook Component Meta (CSF Default Export)
  property_count: 10
  slug: storybook-component-meta
- name: Storybook Story (CSF)
  property_count: 7
  slug: storybook-story
json_structures:
- name: Storybook Csf Structure
  property_count: 0
  slug: storybook-csf-structure
jsonld:
- class_count: 6
  name: Storybook Context
  property_count: 7
  slug: storybook-context
layout: provider
modified: '2026-05-02'
name: Storybook
nav: Providers
network: true
overview: 'Storybook publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Accessibility Testing, Component Documentation, Component Testing, Design Systems, and Front-End Development.


  The Storybook catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Storybook''s developer surface includes documentation, engineering blog, release notes, YouTube channel, and 13 more developer resources.'
plans:
- name: Storybook Plans Pricing
  plan_count: 3
  slug: storybook-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Storybook Rate Limits
  slug: storybook-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Storybook API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: storybook-jsonschema-spectral-rules
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 12
    catalog_gap: 62.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 10.7
    developer_ergonomics: 16.7
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 39.5
  open_source:
    applies: true
    score: 100.0
  previous_composite: 29.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/storybook/refs/heads/main/screenshots/storybook-2026-06-20T194609.png
security:
- kind: domain-security
  name: Storybook Domain Security
  slug: storybook-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: storybook
tags:
- Accessibility Testing
- Component Documentation
- Component Testing
- Design Systems
- Front-End Development
- Open-Source
- React
- UI Components
- Visual Testing
website: https://storybook.js.org/
---
