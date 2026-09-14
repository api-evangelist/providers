---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Tano Agentic Access
  operation_count: 17
  slug: tano-agentic-access
  summary_line: 17 operations · 9 acting
api_count: 1
apis:
- baseURL: https://tano.ai
  baseurl_source: spec
  description: Brand signups for product offerings (Creator Partnership Ads, Content Analysis Framework, Creator Discovery Guide, USA waitlist).
  name: Tano Brand Signups API
  slug: tano-brand-signups-api
- baseURL: https://tano.ai
  baseurl_source: spec
  description: Contact form submissions and updates.
  name: Tano Contact API
  slug: tano-contact-api
- baseURL: https://tano.ai
  baseurl_source: spec
  description: Creator-side signups.
  name: Tano Creator Signups API
  slug: tano-creator-signups-api
- baseURL: https://tano.ai
  baseurl_source: spec
  description: Static discovery files for AI agents (llms.txt, manifests, sitemap).
  name: Tano Discovery API
  slug: tano-discovery-api
- baseURL: https://tano.ai
  baseurl_source: spec
  description: Webinar and event registrations.
  name: Tano Events API
  slug: tano-events-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tano Public Brand Signups API
  slug: open-tano-brand-signups-api
- collection_type: open
  name: Tano Public Brand Signups Contact API
  slug: open-tano-contact-api
- collection_type: open
  name: Tano Public Brand Signups Creator Signups API
  slug: open-tano-creator-signups-api
- collection_type: open
  name: Tano Public Brand Signups Discovery API
  slug: open-tano-discovery-api
- collection_type: open
  name: Tano Public Brand Signups Events API
  slug: open-tano-events-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/tano-agents.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tano-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tano-openapi-overlay.yaml
- group: other
  title: ''
  type: AgentCard
  url: a2a/tano-a2a.yml
- group: company
  title: ''
  type: Website
  url: http://tano.ai
created: '2026-07-17'
description: Tano is a company surfaced as a portfolio company of seedcamp and added to the API Evangelist network as a stub for enrichment. This profile is a lead awaiting the enrichment pipeline.
layout: provider
mcp_servers:
- description: ''
  name: Tano
  slug: tano
modified: '2026-07-17'
name: Tano
nav: Providers
network: true
overview: Tano publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Brand Signups API, Contact API, Creator Signups API, and 2 more. Tagged areas include Company.
random_paper: 14
screenshot: https://raw.githubusercontent.com/api-evangelist/tano/refs/heads/main/screenshots/tano-2026-09-02T162520.png
security:
- kind: authentication
  name: Tano Authentication
  slug: tano-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Tano Domain Security
  slug: tano-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tano
tags:
- Company
website: http://tano.ai
---
