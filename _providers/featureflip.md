---
api_count: 2
apis:
- description: Programmatic access to Featureflip — projects, environments, feature flags, variations, targeting, segments, and SDK keys. Bearer-token auth (ffp_ personal / ffs_ service tokens).
  name: Management API
  slug: management-api
- description: High-performance feature flag evaluation service for SDKs, with client and SDK endpoints for evaluation, identify, streaming, flags, and events.
  name: Evaluation API
  slug: evaluation-api
- description: Documentation for the @featureflip/mcp server, a local stdio process run via npx that calls the Management API on your behalf using a bearer token.
  name: MCP Server (local)
  slug: mcp-server-local
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://featureflip.io/
- group: auth
  title: ''
  type: Authentication
  url: authentication/featureflip-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/featureflip-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/featureflip-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/featureflip-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/featureflip-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/featureflip-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/featureflip-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/featureflip-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/featureflip-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/featureflip-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/featureflip-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/featureflip-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/featureflip-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Rules
  url: rules/featureflip-spectral.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://featureflip.io/docs/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://featureflip.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://featureflip.io/docs/quickstart/javascript/
- group: commercial
  title: ''
  type: Pricing
  url: https://featureflip.io/pricing/
- group: company
  title: ''
  type: Blog
  url: https://featureflip.io/blog/
- group: operate
  title: ''
  type: Support
  url: https://featureflip.io/contact/
- group: start
  title: ''
  type: SignUp
  url: https://app.featureflip.io/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/canopy-labs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://featureflip.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://featureflip.io/privacy/
created: '2026-09-12'
description: Feature flag platform with automated dead-flag cleanup (via a GitHub Action), flat pricing, and API-first, agent-native surfaces. Exposes a Management REST API and a high-performance Evaluation API, both with public OpenAPI contracts, plus official SDKs for 13 languages, OpenFeature providers, a Terraform provider, and a local MCP server.
layout: provider
mcp_servers:
- description: Local Model Context Protocol server that lets AI agents (Claude Code, Cursor, etc.) manage Featureflip flags by calling the Management API on the caller's behalf. It manages flag configuration; it doe
  name: Featureflip MCP Server
  slug: featureflip-mcp-server
modified: '2026-09-13'
name: Featureflip
nav: Providers
network: true
overview: 'Featureflip publishes 2 APIs on the [APIs.io](https://apis.io/) network: Management API and Evaluation API. Tagged areas include feature flags, feature management, feature flag cleanup, progressive delivery, and experimentation.


  The Featureflip catalog on APIs.io includes 1 Spectral governance ruleset.


  Featureflip''s developer surface includes authentication, changelog, documentation, getting-started guide, pricing, engineering blog, support, and 19 more developer resources.'
plans:
- name: Featureflip Plans Pricing
  plan_count: 4
  slug: featureflip-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Featureflip Rate Limits
  slug: featureflip-rate-limits
rules:
- effective_rule_count: 41
  extends:
  - spectral:oas
  name: Featureflip API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: featureflip-spectral
security:
- kind: authentication
  name: Featureflip Authentication
  slug: featureflip-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Featureflip Domain Security
  slug: featureflip-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: featureflip
tags:
- feature flags
- feature management
- feature flag cleanup
- progressive delivery
- experimentation
- feature flags as code
- OpenFeature
- MCP
- developer tools
- DevOps/CI-CD
website: https://featureflip.io/
---
