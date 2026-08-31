---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  scored_at: '2026-08-30'
api_count: 5
apis:
- description: Open-source 9B-parameter image-text-to-text multimodal model designed for digital agents - simple architecture, arbitrary image resolutions, and strong UI/document understanding. Self-hosted only - no
  name: Adept Fuyu-8B Model
  slug: adept-fuyu-8b-model
- description: Open-source 8B-parameter base text generation model with permissive license. Self-hosted only - no managed API.
  name: Adept Persimmon-8B Base Model
  slug: adept-persimmon-8b-base-model
- description: Open-source chat-tuned variant of Persimmon-8B. Self-hosted only - no managed API.
  name: Adept Persimmon-8B Chat Model
  slug: adept-persimmon-8b-chat-model
- description: Research outputs and demos for Adept's ACT-1 and ACT-2 action transformers - foundation models that take actions on software tools. No public commercial API was released.
  name: Adept ACT Research
  slug: adept-act-research
- description: Adept's company and research blog site. After the 2024 Amazon AGI talent move and IP licensing arrangement, the site primarily serves as a historical research record.
  name: Adept Website
  slug: adept-website
artifact_total: 10
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/adept-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adept-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.adept.ai/blog/rss.xml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adeptai
- group: company
  title: ''
  type: Website
  url: https://www.adept.ai/
- group: other
  title: ''
  type: HuggingFace
  url: https://huggingface.co/adept
- group: commercial
  title: ''
  type: Plans
  url: plans/adept-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adept-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/adept-finops.yml
created: '2026-05-08'
description: Adept was an AI research lab building action-taking foundation models (the ACT family) that can use software tools and complete tasks across business applications. In mid-2024, several Adept co-founders and senior researchers joined Amazon's AGI organization in a non-acquisition arrangement, and Amazon licensed Adept's technology. Adept the entity continues to exist, but it has no current public commercial API; its primary remaining footprint is open-source models published on Hugging Face (Fuyu-8B, Persimmon-8B) and historical research outputs (ACT-1, ACT-2).
finops:
- name: Adept Finops
  service_category: AI and Machine Learning
  slug: adept-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/adept.png
layout: provider
modified: '2026-05-08'
name: Adept
nav: Providers
network: true
overview: 'Adept publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Agents, Foundation Models, Action Models, and Workflow-Automation.


  Adept''s developer surface includes engineering blog and 8 more developer resources.'
plans:
- name: Adept Plans Pricing
  plan_count: 2
  slug: adept-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Adept Rate Limits
  slug: adept-rate-limits
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 6
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 15.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adept/refs/heads/main/screenshots/adept-2026-06-20T164644.png
security:
- kind: domain-security
  name: Adept Domain Security
  slug: adept-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Adept Trust Center
  slug: adept-trust-center
  summary_line: SOC 2, ISO 27001
slug: adept
tags:
- Artificial Intelligence
- Agents
- Foundation Models
- Action Models
- Workflow-Automation
- Multimodal
website: https://www.adept.ai/
---
