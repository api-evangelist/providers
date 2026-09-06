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
  band: agent-ready
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Replicant Agentic Access
  operation_count: 2
  slug: replicant-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 2
apis:
- baseURL: https://api.replicant.ai/api/v2
  baseurl_source: declared
  description: The Replicant API from Replicant — 2 operation(s) for replicant.
  name: Replicant Replicant API
  slug: replicant-replicant-api
artifact_total: 9
asyncapis:
- description: ''
  name: Replicant Outbound Call Status Webhooks
  slug: replicant-outbound-call-status-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/replicant-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/replicant-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.replicant.com/
- group: company
  title: ''
  type: Blog
  url: https://www.replicant.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.replicant.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.replicant.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.replicant.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/replicant-ai
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/replicant-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/replicant-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: security/replicant-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/replicant-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/replicant-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.replicant.com/safety-ai-security
- group: design
  title: ''
  type: Conformance
  url: conformance/replicant-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/replicant-domain-security.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/replicant-outbound-api-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/replicant-outbound-api-overlay.yaml
- group: design
  title: ''
  type: Conventions
  url: conventions/replicant-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/replicant-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/replicant-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/replicant-outbound-call-status-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/replicant-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/replicant-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.replicant.com/contact-center-automation/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.replicant.com/contact
created: '2026-07-17'
description: Replicant is an enterprise agentic customer service platform that automates high-volume contact center conversations across voice, chat, and messaging, and analyzes 100% of interactions for QA, compliance, and automation insights. Its two products — Conversation Automation and Conversation Intelligence — replicate top-performing human agents using a hybrid agentic-plus-deterministic architecture with human-in-the-loop escalation, and integrate with existing CCaaS, CRM, telephony, and ticketing stacks. Replicant is telephony-native, runs multi-region on Google Cloud, and is built for SOC 2, HIPAA, PCI, and GDPR requirements. It is sales-led with no public developer portal, but it does publish one machine-readable contract — the Replicant Outbound API (OpenAPI 3.0.0, v2.0.1), served from the provider's own Swagger UI at docs.replicant.ai and live on api.replicant.ai — which places outbound AI voice calls and SMS against a configured campaign and notifies the caller of call status.
image: https://cdn.prod.website-files.com/67977c1e48dbb17d41f9520b/67a0beb2e1e43c91319354bb_Featured-Image.png
layout: provider
modified: '2026-08-14'
name: Replicant
nav: Providers
network: true
overview: 'Replicant publishes 1 API on the [APIs.io](https://apis.io/) network: Replicant API. Tagged areas include Company, Contact Center, Conversational AI, Customer Service, and Voice AI.


  The Replicant catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Replicant''s developer surface includes authentication, engineering blog, pricing, support, and 23 more developer resources.'
plans:
- name: Replicant Plans Pricing
  plan_count: 3
  slug: replicant-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Replicant Rate Limits
  slug: replicant-rate-limits
score:
  band: strong
  composite: 54.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 65.8
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 54.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/replicant/refs/heads/main/screenshots/replicant-2026-08-17T081526.png
security:
- kind: authentication
  name: Replicant Authentication
  slug: replicant-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Replicant Domain Security
  slug: replicant-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Replicant Vulnerability Disclosure
  slug: replicant-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Replicant Trust Center
  slug: replicant-trust-center
  summary_line: SOC 2 Type 2, PCI DSS, HIPAA, GDPR
slug: replicant
tags:
- Company
- Contact Center
- Conversational AI
- Customer Service
- Voice AI
- Contact Center Automation
- Agentic AI
- Conversation Intelligence
website: https://www.replicant.com/
---
