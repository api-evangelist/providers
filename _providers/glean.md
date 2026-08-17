---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 57
  human_in_the_loop: 0
  name: Glean Agentic Access
  operation_count: 61
  slug: glean-agentic-access
  summary_line: 61 operations · 57 acting
api_count: 22
apis:
- description: Run unified semantic and keyword search across all connected enterprise content with permission-aware results, filters, and facets.
  name: Glean Search API
  slug: glean-search-api
- description: Multi-turn generative chat over enterprise content with grounded answers, citations, and tool use.
  name: Glean Chat API
  slug: glean-chat-api
- description: Build and invoke autonomous agents that reason over enterprise data and perform multi-step workflows on behalf of users.
  name: Glean Agents API
  slug: glean-agents-api
- description: Look up people in the enterprise knowledge graph including profile, expertise, org chart relationships, and activity.
  name: Glean People API
  slug: glean-people-api
- description: Read and submit activity signals (views, clicks, edits) that improve personalization and ranking across the Glean instance.
  name: Glean Activity API
  slug: glean-activity-api
- description: Administer governance policies, data classification, and access controls across the Glean instance.
  name: Glean Governance API
  slug: glean-governance-api
- description: The activity API from Glean — 2 operation(s) for activity.
  name: Glean activity API
  slug: glean-activity-api
- description: The agents API from Glean — 5 operation(s) for agents.
  name: Glean agents API
  slug: glean-agents-api
- description: The announcements API from Glean — 3 operation(s) for announcements.
  name: Glean announcements API
  slug: glean-announcements-api
- description: The answers API from Glean — 5 operation(s) for answers.
  name: Glean answers API
  slug: glean-answers-api
- description: The chat API from Glean — 8 operation(s) for chat.
  name: Glean chat API
  slug: glean-chat-api
- description: The collections API from Glean — 8 operation(s) for collections.
  name: Glean collections API
  slug: glean-collections-api
- description: The documents API from Glean — 3 operation(s) for documents.
  name: Glean documents API
  slug: glean-documents-api
- description: The governance API from Glean — 3 operation(s) for governance.
  name: Glean governance API
  slug: glean-governance-api
- description: The insights API from Glean — 1 operation(s) for insights.
  name: Glean insights API
  slug: glean-insights-api
- description: The people API from Glean — 2 operation(s) for people.
  name: Glean people API
  slug: glean-people-api
- description: The pins API from Glean — 5 operation(s) for pins.
  name: Glean pins API
  slug: glean-pins-api
- description: The search API from Glean — 5 operation(s) for search.
  name: Glean search API
  slug: glean-search-api
- description: The shortcuts API from Glean — 5 operation(s) for shortcuts.
  name: Glean shortcuts API
  slug: glean-shortcuts-api
- description: The summarize API from Glean — 1 operation(s) for summarize.
  name: Glean summarize API
  slug: glean-summarize-api
- description: The tools API from Glean — 2 operation(s) for tools.
  name: Glean tools API
  slug: glean-tools-api
- description: The verification API from Glean — 3 operation(s) for verification.
  name: Glean verification API
  slug: glean-verification-api
artifact_total: 48
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Glean Client REST activity API
  slug: open-glean-activity-api
- collection_type: open
  name: Glean Client REST activity agents API
  slug: open-glean-agents-api
- collection_type: open
  name: Glean Client REST activity announcements API
  slug: open-glean-announcements-api
- collection_type: open
  name: Glean Client REST activity answers API
  slug: open-glean-answers-api
- collection_type: open
  name: Glean Client REST activity chat API
  slug: open-glean-chat-api
- collection_type: open
  name: Glean Client REST activity collections API
  slug: open-glean-collections-api
- collection_type: open
  name: Glean Client REST activity documents API
  slug: open-glean-documents-api
- collection_type: open
  name: Glean Client REST activity governance API
  slug: open-glean-governance-api
- collection_type: open
  name: Glean Client REST activity insights API
  slug: open-glean-insights-api
- collection_type: open
  name: Glean Client REST activity people API
  slug: open-glean-people-api
- collection_type: open
  name: Glean Client REST activity pins API
  slug: open-glean-pins-api
- collection_type: open
  name: Glean Client REST activity search API
  slug: open-glean-search-api
- collection_type: open
  name: Glean Client REST activity shortcuts API
  slug: open-glean-shortcuts-api
- collection_type: open
  name: Glean Client REST activity summarize API
  slug: open-glean-summarize-api
- collection_type: open
  name: Glean Client REST activity tools API
  slug: open-glean-tools-api
- collection_type: open
  name: Glean Client REST activity verification API
  slug: open-glean-verification-api
- collection_type: open
  name: Glean Client REST API
  slug: open-glean
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/glean-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/glean-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/glean-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/glean-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/glean-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.glean.com/
- group: other
  title: ''
  type: Developer
  url: https://developers.glean.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.glean.com/api-info/client/getting-started
- group: build
  title: ''
  type: SDKs
  url: https://developers.glean.com/sdks
- group: build
  title: ''
  type: GitHub
  url: https://github.com/gleanwork
- group: company
  title: ''
  type: Blog
  url: https://www.glean.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.glean.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.glean.com/
- group: operate
  title: ''
  type: Support
  url: https://help.glean.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.glean.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.glean.com/legal/customer-terms-of-service
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/glean-technologies/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.glean.com/changelog
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.glean.com/llms.txt
created: '2026-05-23'
description: Glean is an AI-powered work assistant and enterprise search platform that connects to a company's apps and data sources to provide unified search, generative answers, and autonomous agents grounded in enterprise knowledge. Glean exposes a Client API for end-user features (search, chat, agents, answers), an Indexing API for ingesting custom data sources, and Admin and Activity APIs for governance and observability.
finops:
- name: Glean Finops
  service_category: API
  slug: glean-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/glean.png
layout: provider
modified: '2026-05-23'
name: Glean
nav: Providers
network: true
overview: 'Glean publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Search API, Chat API, Agents API, and 19 more. Tagged areas include Agents, AI, Answers, Chat, and Connectors.


  Glean''s developer surface includes authentication, documentation, GitHub presence, engineering blog, pricing, support, changelog, and 12 more developer resources.'
plans:
- name: Glean Plans Pricing
  plan_count: 1
  slug: glean-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 2
  name: Glean Rate Limits
  slug: glean-rate-limits
score:
  band: developing
  composite: 49.7
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 55.2
    developer_ergonomics: 32.6
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 57.9
  previous_composite: 49.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/glean/refs/heads/main/screenshots/glean-2026-06-20T181906.png
security:
- kind: authentication
  name: Glean Authentication
  slug: glean-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Glean Domain Security
  slug: glean-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Glean Vulnerability Disclosure
  slug: glean-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Glean Trust Center
  slug: glean-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: glean
tags:
- Agents
- AI
- Answers
- Chat
- Connectors
- Enterprise Search
- Generative AI
- Indexing
- Knowledge
- RAG
- Search
- Work Assistant
website: https://www.glean.com/
---
