---
api_count: 1
apis:
- baseURL: https://es-pera.org/api/v1
  baseurl_source: declared
  description: 'Open, unauthenticated read-only REST API (GET/HEAD, JSON) over SNS hospital and autonomous-community waiting-list open data. Nine operations across health/releases, hospital entities and metrics, and '
  name: ES·pera Public Data API
  slug: espera-public-data-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/es-pera-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://es-pera.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://es-pera.org/metodologia/
- group: docs
  title: ''
  type: Documentation
  url: https://es-pera.org/metodologia/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/es-pera-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/es-pera-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/es-pera-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/es-pera-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/es-pera-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/es-pera-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/es-pera-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/es-pera-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/es-pera-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/es-pera-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/es-pera-changelog.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/es-pera-mcp.yml
created: '2026-09-13'
description: ES·pera is an independent Spanish-language observatory that gathers scattered official Spanish National Health System (SNS) and autonomous-community publications on healthcare waiting lists and hospital activity, and republishes them as comparable, provenance-preserving open data. It exposes a free, open, unauthenticated read-only REST API (OpenAPI 3.1 at /api/v1) covering hospital entities, national activity metrics and autonomous waiting-list observations, served from immutable content-addressed data releases. Discovery is via an RFC 9727 API catalog, an llms.txt, and a provider-published Agent Skill; there is no MCP server, no A2A agent card, and no client SDK.
image: https://es-pera.org/favicon-espera.svg
layout: provider
modified: '2026-09-13'
name: ES·pera API
nav: Providers
network: true
overview: 'ES·pera API publishes 1 API on the [APIs.io](https://apis.io/) network: ES·pera Public Data API. Tagged areas include healthcare, open data, waiting lists, hospital activity, and Spain.


  ES·pera API''s developer surface includes documentation, authentication, changelog, and 14 more developer resources.'
plans:
- name: Es Pera Plans Pricing
  plan_count: 0
  slug: es-pera-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 2
  name: Es Pera Rate Limits
  slug: es-pera-rate-limits
security:
- kind: authentication
  name: Es Pera Authentication
  slug: es-pera-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Es Pera Domain Security
  slug: es-pera-domain-security
  summary_line: TLSv1.3
slug: es-pera
tags:
- healthcare
- open data
- waiting lists
- hospital activity
- Spain
- public sector
- government data
- SNS
website: https://es-pera.org/
---
