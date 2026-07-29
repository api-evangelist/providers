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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/bolt-new-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bolt-new-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bolt.new/
- group: other
  title: ''
  type: Parent
  url: https://stackblitz.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.bolt.new/
- group: agent
  title: ''
  type: LlmsText
  url: https://support.bolt.new/llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://pricing.bolt.new
- group: start
  title: ''
  type: Signup
  url: https://bolt.new/
- group: other
  title: ''
  type: WebContainerAPI
  url: https://webcontainers.io
- group: build
  title: ''
  type: WebContainerSDK
  url: https://www.npmjs.com/package/@webcontainer/api
- group: build
  title: ''
  type: StackBlitzSDK
  url: https://github.com/stackblitz/sdk
- group: other
  title: ''
  type: OpenSourceRepo
  url: https://github.com/stackblitz/bolt.new
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stackblitz
- group: learn
  title: ''
  type: TutorialKit
  url: https://github.com/stackblitz/tutorialkit
- group: other
  title: ''
  type: Starters
  url: https://github.com/stackblitz/starters
- group: other
  title: ''
  type: WebContainerCore
  url: https://github.com/stackblitz/webcontainer-core
- group: other
  title: ''
  type: Enterprise
  url: https://stackblitz.com/enterprise
- group: other
  title: ''
  type: DesignSystems
  url: https://stackblitz.com/enterprise/design-systems
- group: company
  title: ''
  type: Careers
  url: https://stackblitz.com/careers
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/stackblitz
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/boltdotnew
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/boltdotnew
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@boltdotnew
- group: commercial
  title: ''
  type: Plans
  url: plans/bolt-new-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bolt-new-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bolt-new-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.stackblitz.com/rss.xml
created: '2026-05-08'
description: Bolt.new is StackBlitz's in-browser AI full-stack app builder. From a natural language prompt it generates, edits, runs, and deploys complete web applications inside the user's browser tab using StackBlitz's WebContainer runtime — a WebAssembly-based Node.js operating system that boots a real filesystem, npm/pnpm/yarn package manager, terminal, and live preview without a remote VM. The product targets product managers, entrepreneurs, marketers, agencies, and non-engineer builders with conversational app creation, design-system import from Figma and component libraries (Material UI, Chakra UI, Shadcn/ui), built-in database and authentication, one-click deploy to Netlify or bolt.host, custom domains, GitHub version control, and integrations with Supabase, Stripe, Expo, and MCP servers. Bolt.new itself is a hosted, UI-driven product metered in monthly AI tokens with Free, Pro, Teams, and Enterprise tiers — there is no public REST/HTTP developer API or CLI. StackBlitz separately
  ships the WebContainer API as a JavaScript/TypeScript SDK (npm @webcontainer/api) for embedding the same in-browser dev environment in third-party sites, plus a StackBlitz SDK (@stackblitz/sdk) for programmatically opening projects. The Bolt.new reference codebase is open source under MIT at github.com/stackblitz/bolt.new as a foundation for building custom AI dev agents; the hosted commercial product is closed source.
finops:
- name: Bolt New Finops
  service_category: AI
  slug: bolt-new-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bolt-new.png
layout: provider
modified: '2026-05-25'
name: Bolt.new
nav: Providers
network: true
overview: 'Bolt.new is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI, AI App Builder, No-Code, Low-Code, and Full-Stack.


  Bolt.new''s developer surface includes documentation, pricing, signup flow, YouTube channel, engineering blog, and 22 more developer resources.'
plans:
- name: Bolt New Plans Pricing
  plan_count: 4
  slug: bolt-new-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 2
  name: Bolt New Rate Limits
  slug: bolt-new-rate-limits
score:
  band: emerging
  composite: 22.2
  delta: -1.7
  facets:
    commercial_clarity: 57.9
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 23.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bolt-new/refs/heads/main/screenshots/bolt-new-2026-06-20T173557.png
security:
- kind: domain-security
  name: Bolt New Domain Security
  slug: bolt-new-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bolt New Trust Center
  slug: bolt-new-trust-center
  summary_line: SOC 2, GDPR
slug: bolt-new
tags:
- AI
- AI App Builder
- No-Code
- Low-Code
- Full-Stack
- WebContainers
- In-Browser IDE
- WebAssembly
- Node.js
- StackBlitz
- Generative UI
- Vibe Coding
- Agent
- Netlify
- Supabase
website: https://bolt.new/
---
