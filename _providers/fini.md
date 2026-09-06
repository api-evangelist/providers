---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 39
  human_in_the_loop: 0
  name: Fini Agentic Access
  operation_count: 56
  slug: fini-agentic-access
  summary_line: 56 operations · 39 acting
api_count: 1
apis:
- baseURL: https://api-prod.usefini.com/v2
  baseurl_source: declared
  description: The Agents API from Fini — 1 operation(s) for agents.
  name: Fini Agents API
  slug: fini-agents-api
- baseURL: https://api-prod.usefini.com/v2
  baseurl_source: declared
  description: The Articles API from Fini — 6 operation(s) for articles.
  name: Fini Articles API
  slug: fini-articles-api
- baseURL: https://api-prod.usefini.com/v2
  baseurl_source: declared
  description: The Conversations API from Fini — 3 operation(s) for conversations.
  name: Fini Conversations API
  slug: fini-conversations-api
- baseURL: https://api-prod.usefini.com/v2
  baseurl_source: declared
  description: The Knowledge API from Fini — 5 operation(s) for knowledge.
  name: Fini Knowledge API
  slug: fini-knowledge-api
- baseURL: https://api-prod.usefini.com/v2
  baseurl_source: declared
  description: The Knowledge Folders API from Fini — 4 operation(s) for knowledge folders.
  name: Fini Knowledge Folders API
  slug: fini-knowledge-folders-api
- baseURL: https://api-prod.usefini.com/v2
  baseurl_source: declared
  description: The Prompts API from Fini — 3 operation(s) for prompts.
  name: Fini Prompts API
  slug: fini-prompts-api
- baseURL: https://api-prod.usefini.com/v2
  baseurl_source: declared
  description: The Rules API from Fini — 6 operation(s) for rules.
  name: Fini Rules API
  slug: fini-rules-api
- baseURL: https://api-prod.usefini.com/v2
  baseurl_source: declared
  description: The Sources API from Fini — 5 operation(s) for sources.
  name: Fini Sources API
  slug: fini-sources-api
- baseURL: https://api-prod.usefini.com/v2
  baseurl_source: declared
  description: The Tags API from Fini — 5 operation(s) for tags.
  name: Fini Tags API
  slug: fini-tags-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fini AI Agents API
  slug: open-fini-agents-api
- collection_type: open
  name: Fini AI Agents Articles API
  slug: open-fini-articles-api
- collection_type: open
  name: Fini AI Agents Conversations API
  slug: open-fini-conversations-api
- collection_type: open
  name: Fini AI Agents Knowledge API
  slug: open-fini-knowledge-api
- collection_type: open
  name: Fini AI Agents Knowledge Folders API
  slug: open-fini-knowledge-folders-api
- collection_type: open
  name: Fini AI Agents Prompts API
  slug: open-fini-prompts-api
- collection_type: open
  name: Fini AI Agents Rules API
  slug: open-fini-rules-api
- collection_type: open
  name: Fini AI Agents Sources API
  slug: open-fini-sources-api
- collection_type: open
  name: Fini AI Agents Tags API
  slug: open-fini-tags-api
common:
- group: company
  title: ''
  type: Website
  url: https://usefini.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.usefini.com/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usefini.com/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.usefini.com/en/api-reference/authentication
- group: company
  title: ''
  type: Blog
  url: https://www.usefini.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.usefini.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.usefini.com/company/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usefini.com/security/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usefini.com/security/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/fini-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fini-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fini-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fini-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fini-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/fini-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/fini-openapi-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fini-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fini-well-known.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fini-agentic-access.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fini-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/fini-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fini-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fini-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fini-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/fini-vulnerability-disclosure.yml
created: '2026-07-17'
description: Fini AI provides self-improving AI agents for enterprise customer support across voice, chat, and email. Built on a RAGless retrieval engine, the Fini Agent Loop, a self-updating Knowledge Atlas, and Agentic Actions, Fini understands customer intent, retrieves the right data, and takes action — resolving up to 90% of support tickets at 99% accuracy. It is purpose-built for regulated industries such as fintech, banking, healthcare, insurance, and e-commerce, with PII redaction, audit trails, and guardrails. Fini exposes a public v2 REST API for managing agents, conversations, knowledge (sources, articles, folders), rules, tags, and prompts, and for driving the agent loop through its Generate Answer endpoint. Backed by Y Combinator (S22) and Matrix Partners.
image: https://mintcdn.com/fini/images/shared/logos/fini-light.png
layout: provider
modified: '2026-07-19'
name: Fini
nav: Providers
network: true
overview: 'Fini publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Articles API, Conversations API, and 6 more. Tagged areas include Company, Artificial Intelligence, AI Agents, Customer-Support, and Customer Experience.


  Fini''s developer surface includes documentation, API reference, engineering blog, pricing, signup flow, authentication, and 20 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 59.7
    developer_ergonomics: 16.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 41.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fini/refs/heads/main/screenshots/fini-2026-07-25T214529.png
security:
- kind: authentication
  name: Fini Authentication
  slug: fini-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fini Domain Security
  slug: fini-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Fini Vulnerability Disclosure
  slug: fini-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Fini Trust Center
  slug: fini-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: fini
tags:
- Company
- Artificial Intelligence
- AI Agents
- Customer-Support
- Customer Experience
- Knowledge-Management
- Conversational AI
- Voice AI
- Help Desk
- Regulated Industries
website: https://usefini.com
---
