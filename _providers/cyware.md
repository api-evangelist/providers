---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-08-06'
api_count: 3
apis:
- description: The public Open API for Cyware Intel Exchange, Cyware's threat intelligence platform. Covers threat data objects and their relations, quick-add and detailed STIX intel submission, intel import, enrich
  name: Cyware Intel Exchange (CTIX) v3 Open API
  slug: cyware-intel-exchange-ctix-v3-open-api
- description: The public Open API for Cyware Orchestrate, Cyware's security orchestration, automation and response platform. Covers playbook listing, execution, run logs, node results, exports and bulk termination;
  name: Cyware Orchestrate (CO) Open API
  slug: cyware-orchestrate-co-open-api
- description: Open-source Model Context Protocol server, written in Go and published under MIT by Cyware Labs, that exposes Cyware Intel Exchange and Cyware Orchestrate to LLM agents as MCP tools. Self-hosted along
  name: Cyware MCP Server
  slug: cyware-mcp-server
artifact_total: 9
asyncapis:
- description: ''
  name: Cyware Orchestrate Webhooks
  slug: cyware-orchestrate-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.cyware.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://techdocs.cyware.com/
- group: docs
  title: ''
  type: Documentation
  url: https://techdocs.cyware.com/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://ctixapiv3.cyware.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://techdocs.cyware.com/ctix/en/api-documentation.html
- group: operate
  title: ''
  type: Support
  url: https://www.cyware.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.cyware.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cyware-labs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cyware.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.cyware.com/book-a-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cyware.com/legal/acceptable-use-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cyware.com/legal/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.cyware.com/compliance
- group: auth
  title: ''
  type: TrustCenter
  url: security/cyware-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cyware-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/cyware-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cyware-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cyware-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cyware-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cyware-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cyware-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/cyware-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cyware-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cyware-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cyware-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cyware-orchestrate-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cyware-domain-security.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cyware-intel-exchange-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cyware-orchestrate-overlay.yaml
created: '2026-08-04'
description: Cyware is a New York-headquartered cybersecurity company, founded in 2016, that builds an AI-powered threat intelligence and security operations platform for enterprise SOC teams, ISACs and ISAOs, government agencies, CERTs and MSSPs. The Cyware Intelligence Suite spans Intel Exchange (its threat intelligence platform, formerly CTIX), Collaborate (bi-directional threat sharing for member communities), Orchestrate (security orchestration and automation), Respond (incident case management) and Cyware AI (agentic security analyst workflows). The platform ingests, deduplicates, enriches, scores and operationalizes structured and unstructured cyber threat intelligence using STIX 2.x, TAXII 2.x and MITRE ATT&CK, and pushes it into SIEM, EDR, firewall and ITSM tooling through 400+ integrations. Programmatic access is delivered through the Intel Exchange v3 Open API and the Orchestrate Open API — both tenant-hosted, both authenticated with HMAC-SHA1 signed Open API credentials — plus
  an open-source Model Context Protocol server that exposes threat-intelligence and playbook actions to LLM agents.
image: https://www.cyware.com/assets/images/cyware.svg
layout: provider
mcp_servers:
- description: ''
  name: cyware-mcp.yml
  slug: cyware-mcpyml
modified: '2026-08-04'
name: Cyware
nav: Providers
network: true
overview: 'Cyware publishes 2 APIs on the [APIs.io](https://apis.io/) network: Intel Exchange (CTIX) v3 Open API and Orchestrate (CO) Open API. Tagged areas include threat-intelligence, cyber-threat-intelligence, cybersecurity, security-operations, and threat-intelligence-platform.


  The Cyware catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cyware''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 23 more developer resources.'
random_paper: 86
rate_limits:
- limit_count: 0
  name: Cyware Rate Limits
  slug: cyware-rate-limits
score:
  band: strong
  composite: 56.2
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 66.3
    developer_ergonomics: 60.3
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 28.9
  previous_composite: 56.2
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Cyware Authentication
  slug: cyware-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Cyware Domain Security
  slug: cyware-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Cyware Trust Center
  slug: cyware-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001:2022, VPAT / Section 508, Privacy Shield
slug: cyware
tags:
- threat-intelligence
- cyber-threat-intelligence
- cybersecurity
- security-operations
- threat-intelligence-platform
- stix
- taxii
- mitre-attack
- soar
- security-orchestration
- incident-response
- threat-intelligence-sharing
- isac
- indicators-of-compromise
- mcp
- agentic-ai
website: https://www.cyware.com/
---
