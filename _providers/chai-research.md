---
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chai-research-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chai-research.com/
- group: other
  title: ''
  type: Company
  url: https://forgeglobal.com/chai-research_stock/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.chaiverse.com/
- group: start
  title: ''
  type: Login
  url: https://console.chaiverse.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.chai-research.com/news
- group: operate
  title: ''
  type: Roadmap
  url: https://www.chai-research.com/chai_roadmap_2026.pdf
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chai-research
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chai-research.com/app-eula
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.chai-research.com/
- group: operate
  title: ''
  type: Support
  url: mailto:hello@chai-research.com
- group: build
  title: ''
  type: Packages
  url: packages/chai-research-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chai-research-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/chai-research-lifecycle.yml
coverage:
  checked: '2026-08-09'
  detail: The Chat API documentation host docs.chai-research.com no longer resolves in DNS and the documented POST /v1/chat/completions route now returns a bodyless 404, leaving the Chaiverse developer console as the only live developer surface — and every path on console.chaiverse.com, including /openapi.json, answers HTTP 307 to /login, with the developer key issued only through the Chaiverse Discord bot or a HuggingFace OAuth sign-in.
  evidence:
  - status: 307
    url: https://console.chaiverse.com/openapi.json
  - status: 404
    url: https://api.chai-research.com/v1/chat/completions
  - status: 404
    url: https://www.chaiverse.com/.well-known/agent-card.json
  reason: partner-login
  state: gated
created: '2026-08-09'
description: Chai Research Corp. (CHAI) is a Palo Alto consumer AI company building a character-and-story chat platform, where users create and talk to AI characters on iOS, Android and the web. Founded in 2021 by William Beauchamp, the company trains and serves its own conversational language models on an in-house GPU cluster, and runs Chaiverse — a developer platform where outside model builders submit HuggingFace-hosted language models, have them deployed to real Chai App users, and compete on a public leaderboard. A public Chat API (api.chai-research.com) and a chaiverse pip package were previously documented; both have since been withdrawn — see x-coverage.
image: https://www.chai-research.com/images/chai-logo.svg
layout: provider
modified: '2026-08-09'
name: Chai Research
nav: Providers
network: true
overview: 'Chai Research is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Large Language Models, Conversational AI, and Chatbots.


  Chai Research''s developer surface includes engineering blog, support, and 12 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 13.0
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 13.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Chai Research Domain Security
  slug: chai-research-domain-security
  summary_line: TLSv1.3 · DMARC
slug: chai-research
tags:
- Company
- Artificial Intelligence
- Large Language Models
- Conversational AI
- Chatbots
- Consumer Applications
- Machine-Learning
- Model Hosting
website: https://www.chai-research.com/
---
