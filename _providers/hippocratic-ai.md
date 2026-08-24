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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 13
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hippocratic-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hippocratic-ai-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://hippocraticai.com/feed/
- group: company
  title: ''
  type: Website
  url: https://www.hippocraticai.com/
- group: start
  title: ''
  type: Login
  url: https://safetyportal.hippocraticai.com/signin
- group: start
  title: ''
  type: SafetyPortal
  url: https://safetyportal.hippocraticai.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.hippocraticai.com/contact
- group: company
  title: ''
  type: Careers
  url: https://www.hippocraticai.com/careers
- group: company
  title: ''
  type: Newsroom
  url: https://www.hippocraticai.com/news
- group: other
  title: ''
  type: Research
  url: https://www.hippocraticai.com/research
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hippocratic-ai-health
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/hippocraticai
- group: other
  title: ''
  type: Customers
  url: ''
- group: auth
  title: ''
  type: Authentication
  url: ''
- group: auth
  title: ''
  type: Compliance
  url: ''
- group: other
  title: ''
  type: Funding
  url: ''
- group: agent
  title: ''
  type: LlmsText
  url: https://hippocraticai.com/llms.txt
created: '2026-05-23'
description: Hippocratic AI builds safety-focused generative AI agents for non-diagnostic healthcare tasks, powered by its Polaris constellation architecture. Polaris 5.0 is a multi-trillion-parameter constellation of specialized models clinically validated by U.S.-licensed clinicians. Hippocratic AI sells agents such as Nurse Co-Pilot and AI Front Door to health systems, payors, and life-sciences organizations through enterprise sales rather than a self-service public API.
features:
- description: Multi-trillion-parameter constellation of specialized healthcare models with a large core model and supporting expert models for tasks such as medication, labs, EHR interaction, and empathy.
  name: Polaris Constellation Architecture
- description: Latest generation, a ~5T-parameter constellation built around a 700B-parameter core, reported to outperform major frontier models on clinical accuracy, safety, regulatory compliance, and empathy.
  name: Polaris 5.0
- description: Voice agent for inbound patient phone calls, scheduling, intake, and triage handoff.
  name: AI Front Door
- description: AI nurse agent that supports patient-facing nursing workflows, with launch partners including Cincinnati Children's.
  name: Nurse Co-Pilot
- description: Library of specialized agents across provider, payor, and pharma sectors.
  name: 1000+ Healthcare Agents
- description: Agents validated by more than 7,500 U.S.-licensed clinicians across more than 725,000 test calls.
  name: Clinical Validation
- description: Hippocratic AI explicitly excludes diagnosis, prescription, hospice care, mental health disorders, and pediatric care under age two from agent scope.
  name: Safety Guardrails
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hippocratic-ai.png
layout: provider
modified: '2026-05-23'
name: Hippocratic AI
nav: Providers
network: true
overview: 'Hippocratic AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Generative AI, Healthcare Agents, Clinical AI, and Patient Engagement.


  Hippocratic AI''s developer surface includes engineering blog, authentication, and 11 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 13.0
  delta: 0.0
  facets:
    access_clarity: 14.5
    commercial_clarity: 14.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 28.7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hippocratic-ai/refs/heads/main/screenshots/hippocratic-ai-2026-06-20T182751.png
security:
- kind: domain-security
  name: Hippocratic Ai Domain Security
  slug: hippocratic-ai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Hippocratic Ai Vulnerability Disclosure
  slug: hippocratic-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: hippocratic-ai
tags:
- Healthcare
- Generative AI
- Healthcare Agents
- Clinical AI
- Patient Engagement
- Voice AI
- Safety
- HIPAA
use_cases:
- description: AI Front Door handles inbound patient phone interactions for health systems.
  name: Inbound Patient Calls
- description: Outbound chronic-care management, post-discharge follow-up, and adherence calls.
  name: Care Management
- description: Donor and patient outreach (for example Gift of Life Marrow Registry, with more than 550,000 volunteer donors).
  name: Patient Engagement at Scale
- description: Agentic AI for biopharma and medtech workflows under a global collaboration with BCG.
  name: Biopharma and Medtech
website: https://www.hippocraticai.com/
---
