---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: Cisco AI Defense is the post-acquisition home of Robust Intelligence's AI security technology. It provides runtime protection for AI applications, model validation, algorithmic red teaming, and visibi
  name: Cisco AI Defense
  slug: cisco-ai-defense
- description: 'The Robust Intelligence AI Firewall provided runtime guardrails for LLM and ML applications, screening prompts and responses for prompt injection, PII, toxicity, hallucination, and policy violations. '
  name: AI Firewall (Legacy)
  slug: ai-firewall
- description: Algorithmic AI Red Teaming was Robust Intelligence's automated adversarial testing product for ML and LLM models, generating attacks across data, model, and prompt layers and producing risk reports fo
  name: Algorithmic AI Red Teaming (Legacy)
  slug: algorithmic-red-teaming
artifact_total: 21
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/robust-intelligence-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.robustintelligence.com/
- group: other
  title: ''
  type: CiscoProduct
  url: https://www.cisco.com/site/us/en/products/security/ai-defense/index.html
- group: other
  title: ''
  type: AcquisitionAnnouncement
  url: https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2024/m08/cisco-announces-intent-to-acquire-robust-intelligence-to-deliver-comprehensive-ai-security.html
- group: company
  title: ''
  type: Blog
  url: https://www.robustintelligence.com/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/robust-intelligence/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/robustintelligence
- group: other
  title: ''
  type: AcquiredBy
  url: https://www.cisco.com/
- group: other
  title: ''
  type: AcquisitionNotice
  url: ''
created: '2026-05-23'
description: Robust Intelligence is an AI security company founded in 2019 to defend ML and GenAI systems against adversarial attacks, data poisoning, prompt injection, and unsafe outputs. Its platform combined automated red teaming (Algorithmic AI Red Teaming) with runtime protection (AI Firewall) for LLM and traditional ML applications. Cisco announced the acquisition of Robust Intelligence in August 2024 and the technology now powers the Cisco AI Defense product line, with Robust Intelligence's capabilities integrated into Cisco's broader security portfolio.
features:
- description: Runtime guardrails screening LLM prompts and responses for prompt injection, PII, toxicity, and policy violations.
  name: AI Firewall
- description: Automated adversarial testing of ML and LLM models across data, model, and prompt attack surfaces.
  name: Algorithmic Red Teaming
- description: Pre-production validation of ML and LLM models against safety, security, and quality criteria.
  name: Model Validation
- description: Visibility into AI applications, models, and providers in use across the enterprise.
  name: Shadow AI Discovery
- description: Native integration with Cisco's broader security portfolio post-acquisition.
  name: Cisco Security Cloud Integration
finops:
- name: Robust Intelligence Finops
  service_category: API
  slug: robust-intelligence-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/robust-intelligence.png
integrations:
- description: Native integration with Cisco's broader security platform.
  name: Cisco Security Cloud
- description: Guardrails and red teaming for OpenAI-based applications.
  name: OpenAI
- description: Protection for Anthropic Claude-based applications.
  name: Anthropic
- description: Validation and red teaming of Hugging Face hosted models.
  name: Hugging Face
- description: Integration with AWS SageMaker for model validation workflows.
  name: SageMaker
layout: provider
modified: '2026-05-23'
name: Robust Intelligence
nav: Providers
network: true
overview: 'Robust Intelligence publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Security, Runtime Protection, Algorithmic Red Teaming, LLM Security, and Cisco.


  Robust Intelligence''s developer surface includes engineering blog and 7 more developer resources.'
plans:
- name: Robust Intelligence Plans Pricing
  plan_count: 1
  slug: robust-intelligence-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Robust Intelligence Rate Limits
  slug: robust-intelligence-rate-limits
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 54.0
    catalog_earned_first_party: 0.0
    catalog_gap: 61.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Robust Intelligence Domain Security
  slug: robust-intelligence-domain-security
  summary_line: TLSv1.3 · DMARC
slug: robust-intelligence
tags:
- AI Security
- Runtime Protection
- Algorithmic Red Teaming
- LLM Security
- Cisco
- Acquired
- Guardrails
use_cases:
- description: Protect production LLM and ML applications against adversarial attacks and unsafe outputs.
  name: Enterprise AI Security
- description: Inventory and govern AI usage across the enterprise to meet emerging regulatory requirements.
  name: AI Governance
- description: Run automated adversarial assessments against AI models before deployment.
  name: Pre-production Red Teaming
- description: Enforce policies on prompts and responses in production GenAI applications.
  name: Runtime Guardrails
website: https://www.robustintelligence.com/
---
