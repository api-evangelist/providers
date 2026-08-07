---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 62.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Micro1 Agentic Access
  operation_count: 18
  slug: micro1-agentic-access
  summary_line: 18 operations · 10 acting
api_count: 1
apis:
- description: The micro1 AI Recruiter public REST API. Create conversational AI interviews from a skill list (or from your own custom questions), preview the questions the AI will ask, invite candidates by email, l
  name: micro1 Public API
  slug: micro1-public-api
artifact_total: 6
asyncapis:
- description: ''
  name: Micro1 Webhooks
  slug: micro1-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.micro1.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ai-recruiter.micro1.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://ai-recruiter.micro1.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://ai-recruiter.micro1.ai/api-reference/getting-started/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://ai-recruiter.micro1.ai/api-reference/getting-started/introduction
- group: company
  title: ''
  type: Blog
  url: https://www.micro1.ai/blog
- group: operate
  title: ''
  type: Support
  url: mailto:support@micro1.ai
- group: start
  title: ''
  type: SignUp
  url: https://www.zara.micro1.ai/
- group: start
  title: ''
  type: Login
  url: https://talent.micro1.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.micro1.ai/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.micro1.ai/legal/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/micro1-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/micro1-well-known.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/micro1-a2a.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/micro1-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/micro1-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/micro1-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/micro1-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/micro1-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/micro1-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/micro1-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/micro1-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/micro1-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/micro1-webhooks.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/micro1-ai-recruiter-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/micro1-domain-security.yml
created: '2026-07-31'
description: 'micro1 is an AI-native talent and human-data company. Its AI recruiter, Zara, runs conversational technical interviews at scale — generating role-specific questions from the skills you want tested, branching in real time, adding an optional coding exercise, and returning a structured report with per-skill AI ratings, CEFR-style soft-skill scores, a proctoring integrity score, transcripts and session recordings. The company also operates an expert-human-data business (Realm reinforcement- learning environments, Cortex agent evaluations, and robotics data collection) that supplies training and evaluation data to frontier AI labs. The micro1 Public API exposes the AI-interview platform: create standard or custom-question interviews, invite candidates, list jobs and job applicants, retrieve completed reports and recordings, and register webhooks so an ATS is notified in real time when interviews start, reports are generated, recordings finish processing, or resume scores land.'
image: https://cdn.prod.website-files.com/6a04bd23eb9d40f76dac1249/6a21b7903ec396493b15c2a1_OG%20(52)%20(1).jpg
layout: provider
mcp_servers:
- description: ''
  name: micro1-mcp.yml
  slug: micro1-mcpyml
modified: '2026-07-31'
name: micro1
nav: Providers
network: true
overview: 'micro1 publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Company, recruiting, hiring, ai-interviews, and talent-assessment.


  The micro1 catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  micro1''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 20 more developer resources.'
random_paper: 22
score:
  band: developing
  composite: 47.9
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 65.9
    developer_ergonomics: 67.4
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 7.9
  previous_composite: 47.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Micro1 Authentication
  slug: micro1-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Micro1 Domain Security
  slug: micro1-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: micro1
tags:
- Company
- recruiting
- hiring
- ai-interviews
- talent-assessment
- candidate-screening
- applicant-tracking
- human-resources
- proctoring
- webhooks
- agent-native
- ai-training-data
website: https://www.micro1.ai/
---
