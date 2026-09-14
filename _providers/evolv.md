---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
api_count: 1
apis:
- baseURL: https://participants.evolv.ai
  baseurl_source: declared
  description: The Evolv Participant API is the runtime edge API the client SDKs call to fetch a participant's experiment configuration and allocations for an environment, and to ingest context and behavioral events
  name: Evolv Participant API
  slug: evolv-participant-api
artifact_total: 7
collections:
- collection_type: postman
  name: Evolv
  slug: postman-evolv-participant-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.evolv.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.evolv.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.evolv.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/evolv-ai
- group: build
  title: ''
  type: SDKs
  url: packages/evolv-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/evolv-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/evolv-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/evolv-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/evolv-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/evolv-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/evolv-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/evolv-changelog.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/evolv-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/evolv-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/evolv-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/evolv-domain-security.yml
- group: start
  title: ''
  type: Login
  url: https://app.evolv.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/evolv-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkills
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/evolv-allocate-participant.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/evolv-record-events.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/evolv-offline-preallocations.md
created: '2026-07-17'
description: Evolv AI (formerly Sentient Ascend) is an experience optimization and autonomous experimentation platform that continuously tests and personalizes digital experiences using machine learning. Its Participant API and official client SDKs for JavaScript, iOS, Android, PHP and React allocate visitors to experiment variants, deliver optimized configurations, and ingest behavioral events so AI-driven optimization can evolve web and app experiences without manual A/B-test management. Enterprises use Evolv AI to automate conversion-rate optimization and personalization across their digital properties.
examples:
- key_count: 1
  name: Evolv Configuration Basic Response Example
  slug: evolv-configuration-basic-response-example
image: https://evolv.ai/favicon.ico
layout: provider
modified: '2026-08-13'
name: Evolv
nav: Providers
network: true
overview: 'Evolv publishes 1 API on the [APIs.io](https://apis.io/) network: Participant API. Tagged areas include Experimentation, Optimization, Personalization, A/B Testing, and Machine-Learning.


  Evolv''s developer surface includes documentation, CLI, authentication, sandbox, changelog, and 17 more developer resources.'
plans:
- name: Evolv Plans Pricing
  plan_count: 0
  slug: evolv-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Evolv Rate Limits
  slug: evolv-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/evolv/refs/heads/main/screenshots/evolv-2026-07-25T213820.png
security:
- kind: authentication
  name: Evolv Authentication
  slug: evolv-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Evolv Domain Security
  slug: evolv-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: evolv
tags:
- Experimentation
- Optimization
- Personalization
- A/B Testing
- Machine-Learning
- Conversion Rate Optimization
- Experience Optimization
- Analytics
- Company
website: https://www.evolv.ai
---
