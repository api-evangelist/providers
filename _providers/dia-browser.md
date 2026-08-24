---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 3
apis:
- description: AI-native browser for macOS (Apple Silicon) that turns browsing into a working surface for an embedded assistant. Surfaces contextual chat, Morning Brief, Reports, Better Meetings, Live Work, and spli
  name: Dia Browser
  slug: browser
- description: In-browser AI assistant that can answer questions across open tabs and connected apps, summarize content, and chain context across the browsing session. Exposed to end users; no documented public API.
  name: Dia Assistant
  slug: assistant
- description: User-side connections to GSuite, Slack, Notion, GitHub, and similar productivity apps, used by the Dia assistant to ground answers and build Reports. Configured per-user in the browser.
  name: Dia App Integrations
  slug: integrations
artifact_total: 9
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/dia-browser-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dia-browser-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dia-browser-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.diabrowser.com/
- group: other
  title: ''
  type: Company
  url: https://thebrowser.company/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-browser-company
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/diabrowser
created: '2026-05-23'
description: Dia is The Browser Company's successor browser to Arc, positioned as an AI-native browser that integrates a chat assistant, contextual search across open tabs and connected apps (GSuite, Slack, Notion, GitHub), Morning Brief summaries, automatic Reports, Better Meetings, and Live Work integrations directly into the browsing surface. Currently available on macOS 14+ on Apple Silicon. No public developer REST API or SDK has been published; the product is consumer-facing and integrates with third parties as a user-side agent rather than via developer APIs.
finops:
- name: Dia Browser Finops
  service_category: API
  slug: dia-browser-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dia-browser.png
layout: provider
modified: '2026-05-23'
name: Dia (The Browser Company)
nav: Providers
network: true
overview: Dia (The Browser Company) publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Browser, AI Browser, Agents, Consumer, and The Browser Company.
plans:
- name: Dia Browser Plans Pricing
  plan_count: 1
  slug: dia-browser-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Dia Browser Rate Limits
  slug: dia-browser-rate-limits
score:
  band: emerging
  composite: 17.5
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 17.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dia-browser/refs/heads/main/screenshots/dia-browser-2026-06-20T180005.png
security:
- kind: domain-security
  name: Dia Browser Domain Security
  slug: dia-browser-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dia Browser Vulnerability Disclosure
  slug: dia-browser-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Dia Browser Trust Center
  slug: dia-browser-trust-center
  summary_line: SOC 2
slug: dia-browser
tags:
- Browser
- AI Browser
- Agents
- Consumer
- The Browser Company
website: https://www.diabrowser.com/
---
