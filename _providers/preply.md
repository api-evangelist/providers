---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: false
    consent_identity: true
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.3
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Preply Agentic Access
  operation_count: 2
  slug: preply-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- description: The Chatgpt Openapi API from Preply — 2 operation(s) for chatgpt openapi.
  name: Preply Chatgpt Openapi API
  slug: preply-chatgpt-openapi-api
artifact_total: 7
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Preply plugin Chatgpt Openapi API
  slug: open-preply-chatgpt-openapi-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/preply-find-a-tutor.md
- group: other
  title: ''
  type: Overlay
  url: overlays/preply-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://preply.com
- group: company
  title: ''
  type: Blog
  url: https://preply.com/en/blog/
- group: operate
  title: ''
  type: Support
  url: https://help.preply.com/en/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.preply.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://termsofuse.preply.com/terms_of_use/en_TermsOfService.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://termsofuse.preply.com/terms_of_use/en_PrivacyPolicy.pdf
- group: agent
  title: ''
  type: MCPServer
  url: mcp/preply-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/preply-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/preply-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/preply-security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/preply-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/preply-lifecycle.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/preply-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/preply-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://preply.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/preply-domain-security.yml
created: '2026-07-17'
description: Preply is a global online language-learning marketplace that connects learners with private tutors across dozens of languages, offering one-on-one video lessons, flexible scheduling and a satisfaction-backed tutor-replacement guarantee. Alongside its consumer marketplace, Preply runs Preply Business, an enterprise language-training offering with SSO, automated user provisioning and LMS integrations. Preply exposes a small public, unauthenticated tutor-search API (originally published as an OpenAI/ChatGPT plugin) that lets applications and agents search tutors by subject, price, availability and language and fetch individual tutor profiles. This profile was enriched by the API Evangelist pipeline from Preply's public surface.
image: https://static.preply.com/ds/icons/favicon-ua.ico
layout: provider
mcp_servers:
- description: ''
  name: Preply MCP Server
  slug: preply-mcp-server
modified: '2026-07-20'
name: Preply
nav: Providers
network: true
overview: 'Preply publishes 1 API on the [APIs.io](https://apis.io/) network: Chatgpt Openapi API. Tagged areas include Company, Education, Language Learning, Tutoring, and Marketplace.


  Preply''s developer surface includes engineering blog, support, and 16 more developer resources.'
random_paper: 17
score:
  band: developing
  composite: 40.7
  delta: 0.0
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 16.7
    contract_quality: 44.8
    developer_ergonomics: 8.9
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 21.1
  previous_composite: 40.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Preply Domain Security
  slug: preply-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Preply Vulnerability Disclosure
  slug: preply-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: preply
tags:
- Company
- Education
- Language Learning
- Tutoring
- Marketplace
- EdTech
- Search
website: https://preply.com
---
