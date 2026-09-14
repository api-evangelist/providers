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
api_count: 1
apis:
- baseURL: https://api.worldlabs.ai
  baseurl_source: spec
  description: The credits API from World Labs — 1 operation(s) for credits.
  name: World Labs credits API
  slug: world-labs-credits-api
- baseURL: https://api.worldlabs.ai
  baseurl_source: spec
  description: The Marble API from World Labs — 8 operation(s) for marble.
  name: World Labs Marble API
  slug: world-labs-marble-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Marble Public API v1 credits API
  slug: open-world-labs-credits-api
- collection_type: open
  name: Public API v1 credits Marble API
  slug: open-world-labs-marble-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/world-labs-marble-developer-api.md
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/world-labs-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/world-labs-marble-overlay.yaml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/world-labs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/world-labs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/world-labs-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://worldlabs.ai
created: '2026-07-17'
description: 'World Labs is a company surfaced as a portfolio company of sv-angel and added to the API Evangelist network as a stub for enrichment. Sector: ai. This profile is a lead awaiting the enrichment pipeline.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/world-labs.png
layout: provider
modified: '2026-07-17'
name: World Labs
nav: Providers
network: true
overview: 'World Labs publishes 2 APIs on the [APIs.io](https://apis.io/) network: credits API and Marble API. Tagged areas include Company and Artificial Intelligence.


  World Labs'' developer surface includes authentication and 6 more developer resources.'
random_paper: 7
security:
- kind: authentication
  name: World Labs Authentication
  slug: world-labs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: World Labs Domain Security
  slug: world-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: World Labs Vulnerability Disclosure
  slug: world-labs-vulnerability-disclosure
  summary_line: disclosure policy published
slug: world-labs
tags:
- Company
- Artificial Intelligence
website: https://worldlabs.ai
---
