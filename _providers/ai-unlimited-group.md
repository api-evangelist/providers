---
api_count: 0
artifact_total: 3
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ai-unlimited-group-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ai-unlimited-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aiug.ai/
- group: operate
  title: ''
  type: Support
  url: https://www.travl.app/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.travl.app/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.travl.app/legal/privacy-policy
coverage:
  checked: '2026-09-13'
  detail: 'AI Unlimited Group ships only end-user consumer apps (Lever, Nest Egg, Travl, Resolve Debt) and has no developer program at all; its corporate domain www.aiug.ai now answers every path — including a control path that cannot exist — with an identical 114-byte GoDaddy parking-lander redirect, and api.lever.app, the only API host its DNS names, returns HTTP 503 "This service has been suspended" with the header x-render-routing: suspend.'
  evidence:
  - status: 200
    url: https://www.aiug.ai/
  - status: 503
    url: https://api.lever.app/
  - status: 404
    url: https://www.travl.app/openapi.json
  - status: 404
    url: https://www.travl.app/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-09-13'
description: 'AI Unlimited Group, Inc. (OTC: AIUG) is a West Hollywood, California fintech holding company founded in 2022 as Lever Global Corporation and renamed in July 2024. It markets four consumer-facing, AI-branded platforms — Lever App (student-loan and consumer-debt management), Nest Egg (self-directed investing, via the Nest Egg Securities broker-dealer), Travl.App (travel planning and savings) and Resolve Debt (accounts receivable). All four are end-user mobile and web products; the company operates no developer program, publishes no API reference, and ships no machine-readable contract. As of September 2026 its corporate domain aiug.ai serves a GoDaddy parking lander and the Lever App backend host api.lever.app returns HTTP 503 with x-render-routing: suspend, leaving travl.app as the only live company property.'
layout: provider
modified: '2026-09-13'
name: AI Unlimited Group
nav: Providers
network: true
overview: 'AI Unlimited Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Fintech, Consumer Finance, and Debt Management.


  AI Unlimited Group''s developer surface includes support and 5 more developer resources.'
plans:
- name: Ai Unlimited Group Plans Pricing
  plan_count: 0
  slug: ai-unlimited-group-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Ai Unlimited Group Rate Limits
  slug: ai-unlimited-group-rate-limits
security:
- kind: domain-security
  name: Ai Unlimited Group Domain Security
  slug: ai-unlimited-group-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ai-unlimited-group
tags:
- Company
- Artificial Intelligence
- Fintech
- Consumer Finance
- Debt Management
- Travel
- Investing
- Mobile Apps
website: https://www.aiug.ai/
---
