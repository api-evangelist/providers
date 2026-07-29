---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Arctic Wolf Agentic Access
  operation_count: 5
  slug: arctic-wolf-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 3
apis:
- description: The Attachment API from Arctic Wolf — 1 operation(s) for attachment.
  name: Arctic Wolf Attachment API
  slug: arctic-wolf-attachment-api
- description: The Comment API from Arctic Wolf — 1 operation(s) for comment.
  name: Arctic Wolf Comment API
  slug: arctic-wolf-comment-api
- description: The Ticket API from Arctic Wolf — 3 operation(s) for ticket.
  name: Arctic Wolf Ticket API
  slug: arctic-wolf-ticket-api
artifact_total: 9
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/arctic-wolf-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/arctic-wolf-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/arctic-wolf-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arctic-wolf-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/arctic-wolf-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/arctic-wolf-well-known.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/arctic-wolf-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/arctic-wolf-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/arctic-wolf-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/arctic-wolf-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/arctic-wolf-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/arctic-wolf-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/arctic-wolf-ticket-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.arcticwolf.com/en
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arcticwolf.com/en/developer-and-oem
- group: docs
  title: ''
  type: APIReference
  url: https://docs.arcticwolf.com/en/developer-and-oem/ticket-api/arctic-wolf-ticket-api/api-specifications/ticket-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.arcticwolf.com/en/developer-and-oem/ticket-api/ticket-api-quick-start-guide/use-the-ticket-api
- group: start
  title: ''
  type: Portal
  url: https://portal.arcticwolf.com/
- group: operate
  title: ''
  type: Support
  url: https://docs.arcticwolf.com/en/arctic-wolf-unified-portal
- group: company
  title: ''
  type: Blog
  url: https://arcticwolf.com/resources/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rtkwlf
- group: commercial
  title: ''
  type: Pricing
  url: https://arcticwolf.com/request-demo/
- group: start
  title: ''
  type: SignUp
  url: https://portal.arcticwolf.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arcticwolf.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arcticwolf.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.arcticwolf.com/
- group: auth
  title: ''
  type: Compliance
  url: https://arcticwolf.com/compliance/
- group: auth
  title: ''
  type: Security
  url: https://arcticwolf.com/vulnerability-disclosure
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/arctic-wolf-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/arctic-wolf-llms.txt
created: '2026-07-17'
description: 'Arctic Wolf is a security operations company delivering 24x7 AI-driven managed detection and response (MDR), managed risk, incident response, and endpoint security through its cloud-native Aurora Platform and Concierge Security Team. For developers and OEM partners, Arctic Wolf exposes a set of REST and standards-based APIs via docs.arcticwolf.com and the Unified Portal: a Ticket API for programmatically listing, commenting on, and closing security tickets; a User API and Aurora Endpoint Defense API for user and endpoint management; and Threat Intelligence feed APIs (TAXII 1.1, TAXII 2.1, and a Blocklist API) for consuming indicators into your own security tooling. Authentication uses bearer JWT tokens generated from Personal API Keys in the Unified Portal, with regional service endpoints (US, EU, AU, CA pods).'
image: https://arcticwolf.com/wp-content/uploads/2021/11/AW_LOGO_REVERSE-334.png
layout: provider
mcp_servers:
- description: ''
  name: arctic-wolf-mcp.yml
  slug: arctic-wolf-mcpyml
modified: '2026-07-18'
name: Arctic Wolf
nav: Providers
network: true
overview: 'Arctic Wolf publishes 3 APIs on the [APIs.io](https://apis.io/) network: Attachment API, Comment API, and Ticket API. Tagged areas include Company, Security, Cybersecurity, Managed Detection and Response, and Security Operations.


  Arctic Wolf''s developer surface includes authentication, documentation, API reference, getting-started guide, developer portal, support, engineering blog, and 24 more developer resources.'
random_paper: 62
score:
  band: developing
  composite: 52.7
  delta: -2.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 58.5
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 31.6
  previous_composite: 54.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arctic-wolf/refs/heads/main/screenshots/arctic-wolf-2026-07-25T201101.png
security:
- kind: authentication
  name: Arctic Wolf Authentication
  slug: arctic-wolf-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Arctic Wolf Domain Security
  slug: arctic-wolf-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Arctic Wolf Vulnerability Disclosure
  slug: arctic-wolf-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Arctic Wolf Trust Center
  slug: arctic-wolf-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: arctic-wolf
tags:
- Company
- Security
- Cybersecurity
- Managed Detection and Response
- Security Operations
- Threat Intelligence
- Ticketing
- Endpoint Security
- SOC
website: https://docs.arcticwolf.com/en
---
