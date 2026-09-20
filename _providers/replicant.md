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
  schema_version: '0.2'
  score: 29.7
  scored_at: '2026-09-19'
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
  name: Replicant API
  slug: replicant-replicant-api
artifact_total: 9
asyncapis:
- description: ''
  name: Replicant Outbound Call Status Webhooks
  slug: replicant-outbound-call-status-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/replicant/refs/heads/main/agentic-access/replicant-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/replicant-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/replicant/refs/heads/main/authentication/replicant-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/replicant/refs/heads/main/llms/replicant-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/replicant-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/replicant/refs/heads/main/lifecycle/replicant-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/replicant-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/replicant/refs/heads/main/security/replicant-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/replicant-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/replicant/refs/heads/main/security/replicant-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/replicant-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/replicant/refs/heads/main/security/replicant-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/replicant-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.replicant.com/safety-ai-security
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/replicant/refs/heads/main/conformance/replicant-conformance.yml
  title: ''
  type: Conformance
  url: conformance/replicant-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/replicant/refs/heads/main/security/replicant-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/replicant-domain-security.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/replicant/refs/heads/main/openapi/_original/replicant-outbound-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/replicant-outbound-api-openapi.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/replicant/refs/heads/main/overlays/replicant-outbound-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/replicant-outbound-api-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/replicant/refs/heads/main/conventions/replicant-conventions.yml
  title: ''
  type: Conventions
  url: conventions/replicant-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/replicant/refs/heads/main/errors/replicant-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/replicant-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/replicant/refs/heads/main/data-model/replicant-data-model.yml
  title: ''
  type: DataModel
  url: data-model/replicant-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/replicant/refs/heads/main/asyncapi/replicant-outbound-call-status-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/replicant-outbound-call-status-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/replicant/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/replicant/refs/heads/main/plans/replicant-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/replicant-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/replicant/refs/heads/main/rate-limits/replicant-rate-limits.yml
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
modified: '2026-09-16'
name: Replicant
nav: Providers
network: true
overview: 'Replicant publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Contact Center, Conversational AI, Customer Service, and Voice AI.


  The Replicant catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Replicant''s developer surface includes authentication, engineering blog, pricing, support, and 23 more developer resources.'
plans:
- name: Replicant Plans Pricing
  plan_count: 3
  slug: replicant-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Replicant Rate Limits
  slug: replicant-rate-limits
score:
  band: developing
  composite: 53.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 65.8
    developer_ergonomics: 37.5
    discoverability: 75.9
    operational_transparency: 36.8
  previous_composite: 53.6
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
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
