---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 58.1
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 172
  human_in_the_loop: 5
  name: Armor Agentic Access
  operation_count: 427
  slug: armor-agentic-access
  summary_line: 427 operations · 172 acting · 5 human-in-the-loop
api_count: 16
apis:
- description: The token-based authentication API for the Armor security platform. POST /auth/authorize exchanges user credentials for an authorization code that must be redeemed within two minutes; POST /auth/token
  name: Armor FH-AUTH Security API
  slug: fh-auth-api
- description: The signature-based authentication scheme for the Armor platform, an alternative to FH-AUTH tokens that removes the refresh flow entirely. An API Key ID and Secret Key are generated in the Armor Manag
  name: Armor ARMOR-PSK Security API
  slug: armor-psk-api
- description: Account-level configuration for the Armor security platform. Covers cloud connections (the credentials and subscriptions that link a customer AWS, Azure or Oracle Cloud environment to Armor), secure n
  name: Armor Accounts API
  slug: accounts-api
- description: Fleet management for Armor Agent, the lightweight Windows and Linux workload protection agent formerly sold as Armor Anywhere. Endpoints cover health monitoring status across the agent estate, malware
  name: Armor Agent Management API
  slug: agent-management-api
- description: 'The largest single Armor API surface, covering compliance assessments and cloud security posture management. Endpoints span CSPM connectors, policies, policy controls, control remediation, resources, '
  name: Armor Compliance API
  slug: compliance-api
- description: Container and registry security for the Armor platform, served on a /containers path prefix of the compliance host. Endpoints manage the container security account, the connector that binds a customer
  name: Armor Container Security API
  slug: container-security-api
- description: 'Programmatic access to the security detections Armor raises against a customer environment. Endpoints return individual security detections and their underlying detection events, an overview roll-up, '
  name: Armor Incident Management API
  slug: incident-management-api
- description: A small operational API exposing the Armor Toolbox, the utility surface used to run infrastructure management actions against protected hosts. It is the v2 successor to the much larger v1 Infrastructu
  name: Armor Infrastructure Management API
  slug: infrastructure-management-api
- description: SIEM log ingestion and routing for the Armor platform, and the only v2 Armor API published on an armor.com host as well as the secure-prod.services tier. Endpoints manage log sources and log groups, f
  name: Armor Log Management API
  slug: log-management-api
- description: 'A focused API for reading and updating a user notification preferences within the Armor platform, controlling which security and operational events generate outbound notifications. Authenticated with '
  name: Armor Notifications API
  slug: notifications-api
- description: The subscription API for Armor event delivery. Callers register detection configurations (which security detections should be pushed, with default labels and a transform to reshape the delivered paylo
  name: Armor Webhooks API
  slug: webhooks-api
- description: The unified public API for Armor MDR, spanning six subsystems behind one host. The Armor Intelligence Platform (AIP) endpoints return AI-processed incident analysis and entity threat intelligence. The
  name: Armor MDR Public API
  slug: mdr-public-api
- description: The account-management domain of the original Armor Services API (Swagger 2.0), still published on api.armor.com alongside the newer v2 platform APIs. Fifty-two paths and seventy operations cover acco
  name: Armor Services API v1 - Account Management
  slug: v1-account-management-api
- description: 'The largest Armor API by operation count: ninety-six paths and one hundred and thirty-one operations covering the Armor Enterprise Cloud and Armor Agent infrastructure estate. Endpoints manage virtual'
  name: Armor Services API v1 - Infrastructure
  slug: v1-infrastructure-api
- description: 'The security domain of the v1 Armor Services API: thirty-four paths and thirty-five operations covering security events and alerts, file integrity monitoring, malware and IDS findings, vulnerability s'
  name: Armor Services API v1 - Security
  slug: v1-security-api
- description: 'The support domain of the v1 Armor Services API: sixteen paths and eighteen operations covering support tickets, ticket comments and attachments, and the notification surfaces around them, giving cust'
  name: Armor Services API v1 - Support
  slug: v1-support-api
artifact_total: 21
asyncapis:
- description: ''
  name: Armor Webhooks Events
  slug: armor-webhooks-events
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/armor-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/armor-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/armor-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.armor.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.armor.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.armor.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.armor.com/
- group: company
  title: ''
  type: Blog
  url: https://res.armor.com/resources/?fwp_type=blog&_type=blog
- group: operate
  title: ''
  type: Support
  url: https://www.armor.com/forms/under-attack
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/armor
- group: commercial
  title: ''
  type: Pricing
  url: https://www.armor.com/solutions/pricing
- group: start
  title: ''
  type: SignUp
  url: https://amp.armor.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://armor.pub/docs/Armor-General-Terms-of-Service.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.armor.com/legal/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.armor.com/why-armor/trusted-expertise
- group: operate
  title: ''
  type: StatusPage
  url: https://status.armor.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/armor-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/armor-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/armor-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/armor-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/armor-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/armor-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/armor-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/armor-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/armor-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/armor-webhooks-events.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-06'
description: 'Armor (legal name Armor Defense Inc.) is a cybersecurity company headquartered in Plano, Texas, founded as FireHost in 2009 by Chris Drake and rebranded as Armor as its portfolio expanded from secure cloud hosting into managed security. Armor sells vendor-agnostic, cloud-native managed detection and response (Armor MDR), compliant managed private cloud (Armor Enterprise Cloud), the Armor Agent workload protection agent (formerly Armor Anywhere), and compliance and offensive-security professional services, to more than 1,700 organizations across 40 countries with a 24/7 follow-the-sun SOC operating from Plano, London, Singapore and Pune. Armor publishes a public developer portal at developer.armor.com that serves sixteen machine-readable contracts through ReDoc: four Swagger 2.0 documents for the original v1 Armor Services API on api.armor.com (account management, infrastructure, security and support, 254 operations) and twelve OpenAPI 3.0.3 documents for the v2 platform on
  *.api.secure-prod.services (accounts, agent management, compliance and CSPM, container security, incident management, infrastructure management, log management, notifications, webhooks, the unified MDR public API, and the ARMOR-PSK and FH-AUTH authentication contracts). Armor also publishes a detailed first-party llms.txt at armor.com/llms.txt and holds SOC 2 Type II, HITRUST CSF, PCI DSS Level 1 Service Provider, ISO 27001, TX-RAMP Level 2, HIPAA and Data Privacy Framework attestations.'
image: https://framerusercontent.com/images/iwYUUtUgg7arqxZ6LH5PMsmFouE.png
layout: provider
modified: '2026-08-06'
name: Armor
nav: Providers
network: true
overview: 'Armor publishes 16 APIs on the [APIs.io](https://apis.io/) network, including FH-AUTH Security API, ARMOR-PSK Security API, Accounts API, and 13 more. Tagged areas include Company, Cybersecurity, Managed Detection and Response, Cloud Security, and Compliance.


  The Armor catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Armor''s developer surface includes documentation, API reference, engineering blog, support, pricing, signup flow, authentication, and 20 more developer resources.'
random_paper: 93
scopes:
- name: Armor Scopes
  scope_count: 4
  slug: armor-scopes
  summary_line: 4 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 52.5
  facets:
    commercial_clarity: 52.6
    contract_quality: 62.5
    developer_ergonomics: 54.3
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 28.9
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: authentication
  name: Armor Authentication
  slug: armor-authentication
  summary_line: apiKey/http/oauth2 · 6 schemes
- kind: domain-security
  name: Armor Domain Security
  slug: armor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: armor
tags:
- Company
- Cybersecurity
- Managed Detection and Response
- Cloud Security
- Compliance
- SIEM
- Vulnerability Management
- Endpoint Security
- Threat Intelligence
- Managed Private Cloud
- CSPM
- Container Security
website: https://www.armor.com/
---
