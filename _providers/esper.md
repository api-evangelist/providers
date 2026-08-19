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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.7
  scored_at: '2026-08-19'
api_count: 13
apis:
- description: APIs for application management
  name: Esper Application API
  slug: esper-application-api
- description: APIs for application management
  name: Esper Application V1 API
  slug: esper-application-v1-api
- description: APIs to run device commands. `This version of commands is being deprecated and documentation will be archived soon. Please use Commands V2.`
  name: Esper Commands API
  slug: esper-commands-api
- description: 'Commands V2.0 is to provide advanced device commands capabilities like queuing, support for offline devices, dynamic device set for commands and command history. Commands 2.0 is in active development '
  name: Esper Commands V2 API
  slug: esper-commands-v2-api
- description: APIs for Content management
  name: Esper Content API
  slug: esper-content-api
- description: APIs for device management
  name: Esper Device API
  slug: esper-device-api
- description: APIs for device group management
  name: Esper Device Group API
  slug: esper-device-group-api
- description: The Esper Enterprise APIs to manage the account information set up for your company’s account. Read our Esper Manage documentation or use the Esper Manage Dashboard through the Esper Developer Console
  name: Esper Enterprise API
  slug: esper-enterprise-api
- description: APIs to Esper Compliance Policy
  name: Esper Enterprise Policy API
  slug: esper-enterprise-policy-api
- description: APIs for geofence management
  name: Esper Geofence API
  slug: esper-geofence-api
- description: APIs to run group commands. Command will be run on all the active devices in a group
  name: Esper Group Commands API
  slug: esper-group-commands-api
- description: APIs for Subscription management
  name: Esper Subscription API
  slug: esper-subscription-api
- description: Fetch API token information
  name: Esper Token API
  slug: esper-token-api
artifact_total: 32
asyncapis:
- description: ''
  name: Esper Events Webhooks
  slug: esper-events-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ESPER API REFERENCE Application API
  slug: open-esper-application-api
- collection_type: open
  name: ESPER API REFERENCE Application Application V1 API
  slug: open-esper-application-v1-api
- collection_type: open
  name: ESPER API REFERENCE Application Commands API
  slug: open-esper-commands-api
- collection_type: open
  name: ESPER API REFERENCE Application Commands V2 API
  slug: open-esper-commands-v2-api
- collection_type: open
  name: ESPER API REFERENCE Application Content API
  slug: open-esper-content-api
- collection_type: open
  name: ESPER API REFERENCE Application Device API
  slug: open-esper-device-api
- collection_type: open
  name: ESPER API REFERENCE Application Device Group API
  slug: open-esper-device-group-api
- collection_type: open
  name: ESPER API REFERENCE Application Enterprise API
  slug: open-esper-enterprise-api
- collection_type: open
  name: ESPER API REFERENCE Application Enterprise Policy API
  slug: open-esper-enterprise-policy-api
- collection_type: open
  name: ESPER API REFERENCE Application Geofence API
  slug: open-esper-geofence-api
- collection_type: open
  name: ESPER API REFERENCE Application Group Commands API
  slug: open-esper-group-commands-api
- collection_type: open
  name: ESPER API REFERENCE Application Subscription API
  slug: open-esper-subscription-api
- collection_type: open
  name: ESPER API REFERENCE Application Token API
  slug: open-esper-token-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/esper-deploy-app-to-group.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/esper-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/esper-manage-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/esper-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.esper.io/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/esper-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://esper.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.esper.io/
- group: docs
  title: ''
  type: Documentation
  url: https://help.esper.io/hc/en-us/categories/11385054747153-Developer-Documentation
- group: docs
  title: ''
  type: APIReference
  url: https://api.esper.io/openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://help.esper.io/hc/en-us/articles/14199291792145-Getting-Started-with-APIs
- group: operate
  title: ''
  type: Support
  url: https://help.esper.io/
- group: company
  title: ''
  type: Blog
  url: https://www.esper.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/esper-io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.esper.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://esper.io/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://esper.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.esper.io/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/esper-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/esper-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/esper-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/esper-llms.txt
created: '2026-07-17'
description: 'Esper is the DevOps platform for connected devices, providing cloud-based Android (and edge) device management, application deployment, and remote orchestration for dedicated-device fleets. The Esper Manage REST API lets developers programmatically provision, monitor, and control Android-based dedicated devices running the Esper agent: manage devices and device groups, upload and roll out applications and versions, run device and group commands, configure compliance and enterprise policies, set up geofences, manage content, and subscribe to device events via webhooks. APIs are authenticated with a Bearer API key and served per-tenant on a dedicated Esper Cloud environment, with an official Python SDK (esperclient) and CLI.'
image: https://avatars.githubusercontent.com/u/49017159?v=4
layout: provider
mcp_servers:
- description: ''
  name: esper-mcp.yml
  slug: esper-mcpyml
modified: '2026-07-19'
name: Esper
nav: Providers
network: true
overview: 'Esper publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Application API, Application V1 API, Commands API, and 10 more. Tagged areas include Device Management, Mobile Device Management, Android, DevOps, and Internet of Things.


  The Esper catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Esper''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 15 more developer resources.'
random_paper: 96
score:
  band: developing
  composite: 48.5
  delta: -1.9
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 16.7
    contract_quality: 62.3
    developer_ergonomics: 51.8
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 2.6
  previous_composite: 50.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/esper/refs/heads/main/screenshots/esper-2026-07-25T213623.png
security:
- kind: authentication
  name: Esper Authentication
  slug: esper-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Esper Domain Security
  slug: esper-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Esper Trust Center
  slug: esper-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: esper
tags:
- Device Management
- Mobile Device Management
- Android
- DevOps
- Internet of Things
- Fleet Management
- Enterprise Mobility
- Edge Computing
- Kiosk
website: https://esper.io
---
