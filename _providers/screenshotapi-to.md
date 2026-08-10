---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.7
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Capture URLs or HTML as images or PDFs.
  name: ScreenshotAPI Screenshots API
  slug: screenshotapi-to-screenshots-api
artifact_total: 1
created: '2026-08-02'
description: 'ScreenshotAPI (screenshotapi.to) is a hosted screenshot and PDF capture API — send a URL or raw HTML, get back a PNG, JPEG, WebP or PDF without running browser infrastructure. The contract is deliberately small: one screenshot resource answering both GET and POST, plus a health check. What sets it apart from its size is the agent-readable surface around it — an llms.txt on the root, a 302KB llms-full.txt, a separate docs llms.txt, an agent install guide, a dedicated AI-agents page, and per-page markdown by appending .md to any /docs/ URL. An MCP server exists but runs locally over stdio and is not yet published to npm, so it is described here rather than advertised as a hosted endpoint. Not to be confused with ScreenshotAPI.net, a different company in the same category — see the screenshotapi-net entry.'
layout: provider
modified: '2026-08-02'
name: ScreenshotAPI
nav: Providers
network: true
overview: 'ScreenshotAPI publishes 1 API on the [APIs.io](https://apis.io/) network: Screenshots API. Tagged areas include Screenshots, Website Screenshots, URL to Image, URL to PDF, and HTML to Image.'
random_paper: 48
score:
  band: emerging
  composite: 22.1
  delta: -0.9
  facets:
    commercial_clarity: 0.0
    contract_quality: 59.4
    developer_ergonomics: 0.0
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 23.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
slug: screenshotapi-to
tags:
- Screenshots
- Website Screenshots
- URL to Image
- URL to PDF
- HTML to Image
- Developer Tools
- Web Automation
- Visual Testing
- Agent-readable
---
