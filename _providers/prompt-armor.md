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
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Prompt Armor Agentic Access
  operation_count: 3
  slug: prompt-armor-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.promptarmor.com
  baseurl_source: declared
  description: Analyze LLM input and output through the detector engine.
  name: PromptArmor Analyze API
  slug: prompt-armor-analyze-api
- baseURL: https://api.promptarmor.com
  baseurl_source: declared
  description: Single-call content verdict against the detection engine.
  name: PromptArmor Content Check API
  slug: prompt-armor-content-check-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PromptArmor Analyze API
  slug: open-prompt-armor-analyze-api
- collection_type: open
  name: PromptArmor Analyze Content Check API
  slug: open-prompt-armor-content-check-api
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
overview: 'PromptArmor publishes 2 APIs on the [APIs.io](https://apis.io/) network: Analyze API and Content Check API. Tagged areas include Artificial Intelligence, LLM, Security, Prompt Injection, and Threat Detection.


  PromptArmor''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Prompt Armor Plans Pricing
  plan_count: 2
  slug: prompt-armor-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Prompt Armor Rate Limits
  slug: prompt-armor-rate-limits
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
- Artificial Intelligence
- LLM
- Security
- Prompt Injection
- Threat Detection
website: https://www.promptarmor.com/
---
