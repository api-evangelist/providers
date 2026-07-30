---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Prompt Armor Agentic Access
  operation_count: 3
  slug: prompt-armor-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 2
apis:
- description: Analyze LLM input and output through the detector engine.
  name: PromptArmor Analyze API
  slug: prompt-armor-analyze-api
- description: Single-call content verdict against the detection engine.
  name: PromptArmor Content Check API
  slug: prompt-armor-content-check-api
artifact_total: 10
collections:
- collection_type: open
  name: PromptArmor API
  slug: open-prompt-armor
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/prompt-armor-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/prompt-armor-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prompt-armor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/prompt-armor-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/promptarmor
- group: company
  title: ''
  type: Website
  url: https://www.promptarmor.com/
- group: docs
  title: ''
  type: Documentation
  url: https://promptarmor.readme.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/prompt-armor-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/prompt-armor-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/prompt-armor-finops.yml
created: '2026-06-20'
description: PromptArmor (YC W24) is an LLM application security platform that detects and blocks enterprise-grade threats - indirect prompt injection, data exfiltration, phishing, and system manipulation - in production AI applications. A real-time detection API analyzes LLM inputs and outputs against a continuously updated set of threat detectors before a completion is acted on, returning a fast verdict (for example containsInjection) so applications can block or allow content.
finops:
- name: Prompt Armor Finops
  service_category: Security
  slug: prompt-armor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prompt-armor.png
layout: provider
modified: '2026-06-20'
name: PromptArmor
nav: Providers
network: true
overview: 'PromptArmor publishes 2 APIs on the [APIs.io](https://apis.io/) network: Analyze API and Content Check API. Tagged areas include AI, LLM, Security, Prompt Injection, and Threat Detection.


  PromptArmor''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Prompt Armor Plans Pricing
  plan_count: 2
  slug: prompt-armor-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 2
  name: Prompt Armor Rate Limits
  slug: prompt-armor-rate-limits
score:
  band: thin
  composite: 34.3
  delta: -2.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 60.2
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 36.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/prompt-armor/refs/heads/main/screenshots/prompt-armor-2026-06-20T192253.png
security:
- kind: authentication
  name: Prompt Armor Authentication
  slug: prompt-armor-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Prompt Armor Domain Security
  slug: prompt-armor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Prompt Armor Vulnerability Disclosure
  slug: prompt-armor-vulnerability-disclosure
  summary_line: disclosure policy published
slug: prompt-armor
tags:
- AI
- LLM
- Security
- Prompt Injection
- Threat Detection
website: https://www.promptarmor.com/
---
