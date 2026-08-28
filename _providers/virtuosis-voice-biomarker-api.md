---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 31.0
  scored_at: '2026-08-26'
api_count: 5
apis:
- description: The accounts API from Virtuosis Voice Biomarker API — 1 operation(s) for accounts.
  name: Virtuosis Voice Biomarker API Accounts API
  slug: virtuosis-voice-biomarker-api-accounts-api
- description: The Voice Biomarker Api Default API from Virtuosis Voice Biomarker API — 1 operation(s) for voice biomarker api default.
  name: Virtuosis Voice Biomarker API Voice Biomarker Api Default API
  slug: virtuosis-voice-biomarker-api-default-api
- description: The recordings API from Virtuosis Voice Biomarker API — 2 operation(s) for recordings.
  name: Virtuosis Voice Biomarker API Recordings API
  slug: virtuosis-voice-biomarker-api-recordings-api
- description: The usage API from Virtuosis Voice Biomarker API — 1 operation(s) for usage.
  name: Virtuosis Voice Biomarker API Usage API
  slug: virtuosis-voice-biomarker-api-usage-api
- description: REST API to upload speech recordings and retrieve health, wellbeing, and communication insights via voice biomarker analysis. Bearer token authentication; access gated to approved organizations.
  name: Virtuosis Voice Biomarker API
  slug: virtuosis-voice-biomarker-api
artifact_total: 11
common:
- group: agent
  title: ''
  type: MCPServer
  url: https://docs.virtuosis.ai/_mcp/server
- group: other
  title: ''
  type: Overlay
  url: overlays/virtuosis-voice-biomarker-api-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/virtuosis-voice-biomarker-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/virtuosis-voice-biomarker-api-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/virtuosis-voice-biomarker-api-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/virtuosis-voice-biomarker-api-api-catalog.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/virtuosis-voice-biomarker-api-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/virtuosis-voice-biomarker-api-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/virtuosis-voice-biomarker-api-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/virtuosis-voice-biomarker-api-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/virtuosis-voice-biomarker-api-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/virtuosis-voice-biomarker-api-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/virtuosis-voice-biomarker-api-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/virtuosis-voice-biomarker-api-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/virtuosis-voice-biomarker-api-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/virtuosis-voice-biomarker-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/virtuosis-voice-biomarker-api-rate-limits.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.virtuosis.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.virtuosis.ai/voice-biomarker-api
- group: docs
  title: ''
  type: APIReference
  url: https://docs.virtuosis.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.virtuosis.ai/voice-biomarker-api
- group: operate
  title: ''
  type: Support
  url: https://www.virtuosis.ai/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.virtuosis.ai/#FAQ
- group: company
  title: ''
  type: Blog
  url: https://www.virtuosis.ai/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/virtuosis-ai
- group: start
  title: ''
  type: SignUp
  url: https://www.virtuosis.ai/trial-request
- group: start
  title: ''
  type: Login
  url: https://app.virtuosis.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.virtuosis.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.virtuosis.ai/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.virtuosis.ai/
created: '2026-08-18'
description: Virtuosis exposes a REST API for acoustic/voice-biomarker analysis of speech recordings, delivering health, wellbeing, and communication insights. Applications upload Base64-encoded audio and poll for analysis results across types such as wellbeing, parkinsons, alzheimers, and communication_coach. Access to live API calls requires an approved organization and API key, while documentation, OpenAPI specs, llms.txt, and a hosted MCP server are publicly reachable.
image: https://cdn.prod.website-files.com/6655f0e4b329b0c698166458/66aaae517c99095814345e2e_Virtuosis256.png
layout: provider
mcp_servers:
- description: ''
  name: Virtuosis Voice Biomarker API MCP Server
  slug: virtuosis-voice-biomarker-api-mcp-server
- description: ''
  name: Virtuosis AI Docs MCP Server
  slug: virtuosis-ai-docs-mcp-server
modified: '2026-08-19'
name: Virtuosis Voice Biomarker API
nav: Providers
network: true
overview: 'Virtuosis Voice Biomarker API publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Voice Biomarker Api Default API, Recordings API, and 2 more. Tagged areas include Digital Health, voice biomarkers, speech analysis, acoustic analysis, and Medical Device.


  Virtuosis Voice Biomarker API''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 24 more developer resources.'
plans:
- name: Virtuosis Voice Biomarker Api Plans Pricing
  plan_count: 0
  slug: virtuosis-voice-biomarker-api-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Virtuosis Voice Biomarker Api Rate Limits
  slug: virtuosis-voice-biomarker-api-rate-limits
score:
  band: developing
  composite: 49.3
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 12.1
    contract_quality: 51.2
    developer_ergonomics: 58.9
    discoverability: 92.6
    governance: 12.1
    operational_transparency: 2.6
  previous_composite: 49.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 53.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Virtuosis Voice Biomarker Api Authentication
  slug: virtuosis-voice-biomarker-api-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Virtuosis Voice Biomarker Api Domain Security
  slug: virtuosis-voice-biomarker-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: virtuosis-voice-biomarker-api
tags:
- Digital Health
- voice biomarkers
- speech analysis
- acoustic analysis
- Medical Device
- Mental Health
- Wellbeing
- neurodegenerative screening
- Telehealth
- Remote Monitoring
- communication coaching
- Clinical Research
- Health AI
- Clinical Decision Support
website: https://www.virtuosis.ai/
---
