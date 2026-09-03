---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.4
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Micro1 Agentic Access
  operation_count: 18
  slug: micro1-agentic-access
  summary_line: 18 operations · 10 acting
api_count: 2
apis:
- baseURL: https://public.api.micro1.ai
  baseurl_source: declared
  description: The Interview API from micro1 — 5 operation(s) for interview.
  name: micro1 Interview API
  slug: micro1-interview-api
- baseURL: https://public.api.micro1.ai
  baseurl_source: declared
  description: The Interview Reports API from micro1 — 2 operation(s) for interview reports.
  name: micro1 Interview Reports API
  slug: micro1-interview-reports-api
- baseURL: https://public.api.micro1.ai
  baseurl_source: declared
  description: The Invite Candidate API from micro1 — 2 operation(s) for invite candidate.
  name: micro1 Invite Candidate API
  slug: micro1-invite-candidate-api
- baseURL: https://public.api.micro1.ai
  baseurl_source: declared
  description: The Job API from micro1 — 1 operation(s) for job.
  name: micro1 Job API
  slug: micro1-job-api
- baseURL: https://public.api.micro1.ai
  baseurl_source: declared
  description: The Job Applicant API from micro1 — 3 operation(s) for job applicant.
  name: micro1 Job Applicant API
  slug: micro1-job-applicant-api
- baseURL: https://public.api.micro1.ai
  baseurl_source: declared
  description: The Webhook API from micro1 — 3 operation(s) for webhook.
  name: micro1 Webhook API
  slug: micro1-webhook-api
artifact_total: 12
asyncapis:
- description: ''
  name: Micro1 Webhooks
  slug: micro1-webhooks
collections:
- collection_type: open
  name: micro1 Public API
  slug: open-micro1-ai-recruiter
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
- description: micro1 operates a live, anonymous (unauthenticated) remote MCP server on its documentation host at https://ai-recruiter.micro1.ai/mcp. It responded to a real `initialize` handshake and a real `tools/l
  name: micro1 API
  slug: micro1-api
modified: '2026-07-31'
name: micro1
nav: Providers
network: true
overview: 'micro1 publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Interview API, Interview Reports API, Invite Candidate API, and 3 more. Tagged areas include Company, Recruiting, Hiring, AI Interviews, and Talent Assessment.


  The micro1 catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  micro1''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 20 more developer resources.'
random_paper: 20
score:
  band: developing
  composite: 43.1
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 62.4
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 43.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/micro1/refs/heads/main/screenshots/micro1-2026-08-07T172821.png
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
- Recruiting
- Hiring
- AI Interviews
- Talent Assessment
- Candidate Screening
- Applicant Tracking
- Human Resources
- Proctoring
- Webhook
- agent-native
- AI Training Data
website: https://www.micro1.ai/
---
