---
api_count: 2
apis:
- description: REST API for machine-verifiable capture and preflight verification of public web sources, with x402 payment-gated access. Includes capture, preflight/guard, guarded-action pilot, quote, proofs, and de
  name: DELTA Witness API
  slug: delta-witness-api
- baseURL: https://delta-witness-partner-gateway.ruphussten.workers.dev
  baseurl_source: declared
  description: Authenticated reseller rail (apiKey x-delta-partner-secret) for DELTA Capture, Guard, and finite prepaid recurring Watch. Marketplace billing must complete before calling this gateway.
  name: DELTA Witness Partner Gateway
  slug: delta-witness-partner-gateway
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://delta-witness-api.ruphussten.workers.dev
- group: auth
  title: ''
  type: DomainSecurity
  url: security/delta-witness-domain-security.yml
- group: build
  title: ''
  type: SDKs
  url: packages/delta-witness-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/delta-witness-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/delta-witness-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/delta-witness-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/delta-witness-a2a.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/delta-witness-well-known.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/delta-witness-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/delta-witness-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/delta-witness-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/delta-witness-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/delta-witness-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/delta-witness-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/delta-witness-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/delta-witness-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/delta-witness-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/15998194110/delta-witness
created: '2026-09-11'
description: Machine-verifiable capture and preflight verification of public web sources. Returns timestamped content hashes plus a public verifier, keeping raw capture artifacts private. Access is payment-gated via the x402 v2 protocol using USDC on Base mainnet. Proves observation and change, not truth.
layout: provider
mcp_servers:
- description: First-party MCP server exposing the paid DELTA Witness Capture and Guard (preflight) tools for public-source observation before autonomous actions.
  name: DELTA Witness MCP
  slug: delta-witness-mcp
modified: '2026-09-11'
name: DELTA Witness — Trust Layer for Autonomous Actions
nav: Providers
network: true
overview: 'DELTA Witness — Trust Layer for Autonomous Actions publishes 2 APIs on the [APIs.io](https://apis.io/) network: DELTA Witness API and DELTA Witness Partner Gateway. Tagged areas include web-verification, proof-of-observation, page-state-monitoring, content-hashing, and agent-guardrails.


  DELTA Witness — Trust Layer for Autonomous Actions'' developer surface includes authentication and 18 more developer resources.'
plans:
- name: Delta Witness Plans Pricing
  plan_count: 3
  slug: delta-witness-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Delta Witness Rate Limits
  slug: delta-witness-rate-limits
security:
- kind: authentication
  name: Delta Witness Authentication
  slug: delta-witness-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Delta Witness Domain Security
  slug: delta-witness-domain-security
  summary_line: TLSv1.3 · DMARC
slug: delta-witness
tags:
- web-verification
- proof-of-observation
- page-state-monitoring
- content-hashing
- agent-guardrails
- preflight-checks
- x402-payments
- pay-per-use
- base-usdc
- autonomous-agents
- mcp
- a2a
- agent-skill
- trust-and-safety
website: https://delta-witness-api.ruphussten.workers.dev
---
