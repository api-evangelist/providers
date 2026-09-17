---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/taskhuman/refs/heads/main/security/taskhuman-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/taskhuman-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://taskhuman.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/taskhuman/refs/heads/main/lifecycle/taskhuman-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/taskhuman-lifecycle.yml
coverage:
  checked: '2026-08-29'
  detail: 'TaskHuman ceased operations and locked its own site down: every path on taskhuman.com now returns HTTP 401 behind an nginx HTTP Basic auth wall (realm "taskhuman2pro"), the API hosts recorded in certificate transparency (api.taskhuman.com, api.prod.taskhuman.com) no longer resolve, app.taskhuman.com and admin.taskhuman.com are dangling CNAMEs at deleted AWS endpoints, and status.taskhuman.com redirects to Atlassian''s unclaimed-Statuspage landing page.'
  evidence:
  - status: 401
    url: https://taskhuman.com/
  - status: 401
    url: https://taskhuman.com/robots.txt
  - status: 0
    url: https://api.taskhuman.com/
  - status: 200
    url: https://resources.taskhuman.com/
  reason: defunct
  state: none
created: '2026-08-29'
description: TaskHuman was a mobile-first, on-demand human coaching platform that connected employees with live 1:1 video coaching across wellbeing, fitness, leadership, professional growth, sales and mentorship topics, sold to employers as a benefit and delivered through iOS, Android and web apps plus Slack and Microsoft Teams integrations. The San Francisco Bay Area company raised roughly $35M from investors including U.S. Venture Partners and Madrona and marketed a coach network spanning more than a thousand skill areas. The company ceased operations in 2026; as of this profile the entire taskhuman.com origin answers HTTP 401 behind an nginx HTTP Basic authentication wall and the product's API and application hosts no longer resolve, so no developer program, documentation or machine-readable contract remains reachable.
layout: provider
modified: '2026-09-15'
name: TaskHuman
nav: Providers
network: true
overview: TaskHuman is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Coaching, Human Resources, Employee Benefits, and Wellbeing.
random_paper: 4
security:
- kind: domain-security
  name: Taskhuman Domain Security
  slug: taskhuman-domain-security
  summary_line: TLSv1.3 · DMARC
slug: taskhuman
tags:
- Company
- Coaching
- Human Resources
- Employee Benefits
- Wellbeing
- Learning and Development
- Video
- Defunct
website: https://taskhuman.com/
---
