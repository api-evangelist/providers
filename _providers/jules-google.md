---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Alpha REST API for Google's Jules autonomous coding agent. Exposes Sources (connected GitHub repositories), Sessions (units of work against a source with a prompt and optional plan-approval workflow),
  name: Jules API
  slug: jules-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jules-google-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jules.google
- group: other
  title: ''
  type: WebApp
  url: https://jules.google.com
- group: docs
  title: ''
  type: Documentation
  url: https://jules.google/docs/
- group: docs
  title: ''
  type: APIDocumentation
  url: https://developers.google.com/jules/api
- group: docs
  title: ''
  type: APIReference
  url: https://developers.google.com/jules/api/reference/rest
- group: build
  title: ''
  type: CLI
  url: https://jules.google/docs/cli/reference/
- group: build
  title: ''
  type: CLIExamples
  url: https://jules.google/docs/cli/examples/
- group: build
  title: ''
  type: GeminiCLIExtension
  url: https://github.com/gemini-cli-extensions/jules
- group: commercial
  title: ''
  type: Pricing
  url: https://jules.google/#pricing
- group: company
  title: ''
  type: Blog
  url: https://blog.google/technology/google-labs/jules/
- group: other
  title: ''
  type: Announcement
  url: https://developers.googleblog.com/en/meet-jules-tools-a-command-line-companion-for-googles-async-coding-agent/
- group: other
  title: ''
  type: GoogleLabs
  url: https://labs.google
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policies.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: other
  title: ''
  type: Company
  url: https://about.google
created: '2026-05-24'
description: 'Jules is Google''s autonomous, asynchronous AI coding agent, developed inside Google Labs and powered by the Gemini family of models (currently Gemini 2.5 Pro on the free tier and Gemini 3 Pro on paid tiers). Jules connects to a user''s GitHub repositories, clones the target repo into a sandboxed Google Cloud VM, generates a multi-step plan, and then executes coding tasks such as bug fixes, refactors, dependency bumps, test authoring, and small feature builds, ultimately opening a pull request for human review. Jules ships three surfaces beyond the web app at jules.google.com: a documented REST API in alpha at jules.googleapis.com/v1alpha (Sources, Sessions, Activities) authenticated via X-Goog-Api-Key, a lightweight CLI called Jules Tools installable via npm, and a Gemini CLI extension that exposes Jules as a /jules slash command. Access is gated to Google account holders and the API is experimental. Jules is sold as part of the Google AI subscription bundles, with a free
  introductory plan (15 tasks/day, 3 concurrent), Google AI Pro at $19.99/month (100 tasks/day, 15 concurrent, Gemini 3 Pro), and Google AI Ultra at $124.99/month (300 tasks/day, 60 concurrent, priority Gemini 3 Pro access).'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jules-google.png
layout: provider
modified: '2026-05-24'
name: Jules
nav: Providers
network: true
overview: 'Jules publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Coding Agent, Autonomous Agent, Asynchronous Agent, and Developer Tools.


  Jules'' developer surface includes documentation, API reference, CLI, pricing, engineering blog, and 11 more developer resources.'
random_paper: 74
score:
  band: emerging
  composite: 18.0
  delta: -2.4
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 20.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jules-google/refs/heads/main/screenshots/jules-google-2026-06-20T183823.png
security:
- kind: domain-security
  name: Jules Google Domain Security
  slug: jules-google-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jules-google
tags:
- Artificial Intelligence
- Coding Agent
- Autonomous Agent
- Asynchronous Agent
- Developer Tools
- Code Generation
- Pull Requests
- GitHub
- Gemini
- Google Labs
- Software Development Lifecycle
- DevOps
website: https://jules.google
---
