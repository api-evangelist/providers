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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-08-11'
api_count: 2
apis:
- description: Wholesale reseller API for domain-name lookup, registration, transfer, renewal, DNS-zone management and TLS/SSL certificate ordering. An XML-over-HTTPS POST protocol authenticated with a reseller user
  name: OpenSRS Domains and TLS/SSL API
  slug: opensrs-domains-and-tlsssl-api
- description: The OpenSRS Mail API is the provisioning interface for the OpenSRS hosted email system — create, modify and delete mailboxes, aliases, domains and other aspects of the service. A stateless web service
  name: OpenSRS Email API (OMA)
  slug: opensrs-email-api-oma
artifact_total: 6
asyncapis:
- description: ''
  name: Tucows Opensrs Domains Events
  slug: tucows-opensrs-domains-events
common:
- group: company
  title: ''
  type: Website
  url: https://tucows.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://opensrs.com
- group: docs
  title: ''
  type: Documentation
  url: https://domains.opensrs.guide
- group: docs
  title: ''
  type: APIReference
  url: https://domains.opensrs.guide/docs/quickstart
- group: start
  title: ''
  type: GettingStarted
  url: https://domains.opensrs.guide/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://support.opensrs.com/support/home
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tucows
- group: operate
  title: ''
  type: StatusPage
  url: https://status.opensrs.com
- group: commercial
  title: ''
  type: Pricing
  url: https://opensrs.com/domains/pricing/
- group: start
  title: ''
  type: Login
  url: https://manage.opensrs.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://opensrs.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://opensrs.com/payment-terms/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tucows-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/tucows-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tucows-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tucows-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tucows-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/tucows-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tucows-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tucows-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tucows-opensrs-domains-events.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tucows-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tucows-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tucows-domain-security.yml
created: '2026-07-17'
description: Tucows is one of the world's largest internet-services and domain companies. Its OpenSRS division runs a wholesale reseller platform for domain-name registration, DNS, TLS/SSL certificates and hosted email, exposed through the OpenSRS API (an XML-over-HTTPS reseller protocol) and the OpenSRS Mail API (OMA). Tucows also operates Wavelo, a telecom BSS/OSS billing, provisioning and subscriber-management platform for communication service providers, and the Ting Internet fiber business. This profile captures the public OpenSRS developer surface — the domains/SSL API, the email provisioning API, authentication, error codes, sandbox, events and lifecycle. Tucows is a Union Square Ventures portfolio company.
image: https://files.readme.io/fd0f1b4-small-OpenSRS_knowledgebase_1.png
layout: provider
mcp_servers:
- description: ''
  name: tucows-mcp.yml
  slug: tucows-mcpyml
modified: '2026-07-21'
name: Tucows
nav: Providers
network: true
overview: 'Tucows publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure, Domains, DNS, and SSL.


  The Tucows catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tucows'' developer surface includes documentation, API reference, getting-started guide, support, pricing, authentication, sandbox, and 18 more developer resources.'
random_paper: 97
score:
  band: developing
  composite: 44.9
  delta: -0.9
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.6
    developer_ergonomics: 60.3
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 36.8
  previous_composite: 45.8
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Tucows Authentication
  slug: tucows-authentication
  summary_line: apiKey/signature · 2 schemes
- kind: domain-security
  name: Tucows Domain Security
  slug: tucows-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tucows
tags:
- Company
- Infrastructure
- Domains
- DNS
- SSL
- Email
- Registrar
- Telecom
website: https://tucows.com
---
