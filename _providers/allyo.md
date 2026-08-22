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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/allyo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.allyo.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/allyo
- group: company
  title: ''
  type: Twitter
  url: https://x.com/allyoai
coverage:
  checked: '2026-08-10'
  detail: AllyO was acquired by HireVue in October 2020 and no longer exists as an independent company — www.allyo.com 301-redirects to hirevue.com/platform/conversational-ai-and-automation, the apex allyo.com returns 502, api.allyo.com resolves only to an internal VPN load balancer that never completes a TLS handshake, and the one surviving host, services.allyo.com, is the login-gated "HireVue Assistant Dashboard" customer app with no public developer surface.
  evidence:
  - status: 301
    url: https://www.allyo.com/
  - status: 502
    url: https://allyo.com/
  - status: 0
    url: https://api.allyo.com/
  - status: 200
    url: https://services.allyo.com/dashboard/list/
  - status: 404
    url: https://services.allyo.com/openapi.json
  - status: 403
    url: https://services.allyo.com/graphql
  - status: 404
    url: https://www.allyo.com/.well-known/agent-card.json
  - status: 404
    url: https://www.allyo.com/llms.txt
  - status: 0
    url: https://status.allyo.com/
  reason: defunct
  state: none
created: '2026-07-17'
description: AllyO is an HR-tech company, founded in 2016 in Palo Alto, California, that built a conversation-first, AI recruiting chatbot and automation platform for high-volume hiring. Its chatbot let candidates apply to jobs, answer common questions, get screened, and schedule interviews via text and web chat 24/7, with integrations into applicant tracking systems, job boards, and background-check providers. AllyO raised roughly $64M in venture funding (including a $45M round in 2019 backed by investors such as Sapphire Ventures) before being acquired by HireVue in October 2020. The AllyO product now lives inside HireVue as its Conversational AI and Automation offering; www.allyo.com 301-redirects to HireVue and AllyO no longer operates an independent public developer or API surface. This profile is retained as an acquired-company record in the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/allyo.png
layout: provider
modified: '2026-08-10'
name: AllyO
nav: Providers
network: true
overview: AllyO is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hr Tech, Recruiting, Conversational AI, and Chatbot.
random_paper: 20
score:
  band: minimal
  composite: 5.0
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/allyo/refs/heads/main/screenshots/allyo-2026-07-25T195728.png
security:
- kind: domain-security
  name: Allyo Domain Security
  slug: allyo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: allyo
tags:
- Company
- Hr Tech
- Recruiting
- Conversational AI
- Chatbot
- Hiring Automation
- Applicant Tracking
- Acquired
website: https://www.allyo.com/
---
