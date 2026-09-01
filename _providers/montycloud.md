---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.6
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The tenant-scoped REST API behind the MontyCloud DAY2 platform. Requests are authenticated with an API key and API secret key issued in the DAY2 platform and are scoped to a tenant via the x-tenant-id
  name: MontyCloud DAY2 API
  slug: montycloud-day2-api
- description: 'MontyCloud''s hosted, remote Model Context Protocol server for the DAY2 platform. MontyCloud''s own MCP Server Security Statement places it at the api.montycloud.com endpoint, states it is cloud-hosted '
  name: MontyCloud CloudOps MCP Server
  slug: montycloud-cloudops-mcp-server
artifact_total: 9
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/montycloud-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/montycloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://montycloud.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.montycloud.com/support/solutions
- group: operate
  title: ''
  type: Support
  url: https://support.montycloud.com/support/home
- group: company
  title: ''
  type: Blog
  url: https://montycloud.com/category/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://montycloud.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/montycloud
- group: commercial
  title: ''
  type: Pricing
  url: https://montycloud.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://montycloud.com/msp-free-trial/
- group: start
  title: ''
  type: Login
  url: https://app.montycloud.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://montycloud.com/wp-content/uploads/2025/10/2026.08-MontyCloud-Subscription-Terms.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://montycloud.com/wp-content/uploads/2025/09/platform-privacy-policy.pdf
- group: auth
  title: ''
  type: Compliance
  url: conformance/montycloud-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/montycloud-conformance.yml
- group: auth
  title: ''
  type: Security
  url: https://montycloud.com/data-security-statement/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/montycloud-vulnerability-disclosure.yml
- group: build
  title: ''
  type: Packages
  url: packages/montycloud-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/montycloud-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/montycloud-well-known.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/montycloud-plans-pricing.yml
- group: company
  title: ''
  type: Newsroom
  url: https://montycloud.com/company/newsroom/
created: '2026-08-26'
description: 'MontyCloud is a Bellevue, Washington software company whose DAY2 platform is a no-code, autonomous CloudOps product for AWS-focused managed service providers and enterprise cloud teams. DAY2 connects to customer AWS (and Azure) accounts through a scoped cross-account IAM role and delivers multi-tenant inventory and discovery, AWS Well-Architected Framework Reviews, compliance and security bots, patching and server management, cost and AWS Billing Conductor reporting, MAP project tracking, blueprints and governance automation. The platform is programmable: MontyCloud publishes a first-party Python SDK and CLI (`day2` on PyPI) against a tenant-scoped REST API at api.montycloud.com, and ships a hosted CloudOps MCP Server so AI agents can drive cloud operations directly. MontyCloud is an AWS Cloud Operations Software Competency and AWS Built-in partner, is SOC 2 Type II audited and GDPR aligned, and also open-sources Moya, a multi-agent orchestration framework.'
image: https://montycloud.com/wp-content/uploads/2025/07/full-color-favicon.svg
layout: provider
mcp_servers:
- description: ''
  name: MontyCloud CloudOps MCP Server
  slug: montycloud-cloudops-mcp-server
modified: '2026-08-26'
name: MontyCloud
nav: Providers
network: true
overview: 'MontyCloud publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud, Cloud Operations, Managed Service Providers, Governance, and Compliance.


  MontyCloud''s developer surface includes documentation, support, engineering blog, pricing, signup flow, and 17 more developer resources.'
plans:
- name: Montycloud Plans Pricing
  plan_count: 3
  slug: montycloud-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Montycloud Rate Limits
  slug: montycloud-rate-limits
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 15
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 37.2
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Montycloud Authentication
  slug: montycloud-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Montycloud Domain Security
  slug: montycloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Montycloud Vulnerability Disclosure
  slug: montycloud-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Montycloud Trust Center
  slug: montycloud-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: montycloud
tags:
- Cloud
- Cloud Operations
- Managed Service Providers
- Governance
- Compliance
- Cost Management
- Artificial Intelligence
- Agents
- MCP
- Multi-Tenant
- Infrastructure
website: https://montycloud.com/
---
