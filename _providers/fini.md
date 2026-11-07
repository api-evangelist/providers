---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 38
  human_in_the_loop: 0
  name: Fini Agentic Access
  operation_count: 56
  slug: fini-agentic-access
  summary_line: 56 operations · 38 acting
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
artifact_total: 29
collections:
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
- group: commercial
  href: https://artifacts.apis.io/fini/plans/fini-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fini-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/fini/capabilities/fini-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/fini-capability-edges.yml
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
  href: https://artifacts.apis.io/fini/authentication/fini-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fini-authentication.yml
- group: design
  href: https://artifacts.apis.io/fini/conventions/fini-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fini-conventions.yml
- group: design
  href: https://artifacts.apis.io/fini/errors/fini-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fini-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fini/lifecycle/fini-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fini-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/fini/data-model/fini-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fini-data-model.yml
- group: agent
  href: https://artifacts.apis.io/fini/mcp/fini-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/fini-mcp.yml
- group: agent
  href: https://artifacts.apis.io/fini/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/fini/overlays/fini-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fini-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/fini/llms/fini-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fini-llms.txt
- group: agent
  href: https://artifacts.apis.io/fini/well-known/fini-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fini-well-known.yml
- group: agent
  href: https://artifacts.apis.io/fini/agentic-access/fini-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fini-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/fini/conformance/fini-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fini-conformance.yml
- group: auth
  href: https://artifacts.apis.io/fini/security/fini-trust-center.yml
  title: ''
  type: Compliance
  url: security/fini-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/fini/security/fini-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/fini-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/fini/security/fini-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fini-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/fini/security/fini-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/fini-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/fini/security/fini-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/fini-vulnerability-disclosure.yml
created: '2026-07-17'
description: Fini AI provides self-improving AI agents for enterprise customer support across voice, chat, and email. Built on a RAGless retrieval engine, the Fini Agent Loop, a self-updating Knowledge Atlas, and Agentic Actions, Fini understands customer intent, retrieves the right data, and takes action — resolving up to 90% of support tickets at 99% accuracy. It is purpose-built for regulated industries such as fintech, banking, healthcare, insurance, and e-commerce, with PII redaction, audit trails, and guardrails. Fini exposes a public v2 REST API for managing agents, conversations, knowledge (sources, articles, folders), rules, tags, and prompts, and for driving the agent loop through its Generate Answer endpoint. Backed by Y Combinator (S22) and Matrix Partners.
finops:
- has_sources: true
  method: derived
  name: Fini Finops
  primary_unit: resolved ticket
  service_category: ''
  slug: fini-finops
  template: false
image: https://mintcdn.com/fini/images/shared/logos/fini-light.png
layout: provider
modified: '2026-07-19'
name: Fini
nav: Providers
network: true
overview: 'Fini publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Articles API, Conversations API, and 6 more. Tagged areas include Company, Artificial Intelligence, AI Agents, Customer Service, and Customer Experience.


  The Fini catalog on APIs.io includes 1 Spectral governance ruleset.


  Fini''s developer surface includes documentation, API reference, engineering blog, pricing, signup flow, authentication, and 22 more developer resources.'
plans:
- name: Fini Plans Pricing
  plan_count: 3
  slug: fini-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: Fini API Rules
  rule_count: 68
  severity_counts:
    error: 65
    hint: 0
    info: 1
    warn: 2
  slug: fini-rules
score:
  band: strong
  composite: 56.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.8
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 54.0
    developer_ergonomics: 35.1
    discoverability: 73.2
    operational_transparency: 10.5
  previous_composite: 53.0
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
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 32.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/fini/fini-2026-07-25T214529.png
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
skill_count: 3
skills:
- name: Answer a customer question with a Fini agent
  slug: fini-answer-customer-question
- name: Export Fini conversations for QA and analytics
  slug: fini-export-conversations
- name: Ingest sources and publish knowledge to a Fini agent
  slug: fini-ingest-and-publish-knowledge
slug: fini
tags:
- Company
- Artificial Intelligence
- AI Agents
- Customer Service
- Customer Experience
- Knowledge Management
- Conversational AI
- Voice AI
- Help Desk
- Regulated Industries
website: https://usefini.com
---
