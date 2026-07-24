---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Cognition Labs Agentic Access
  operation_count: 26
  slug: cognition-labs-agentic-access
  summary_line: 26 operations · 14 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: Upload and download files for Devin to work with.
  name: Cognition Labs Attachments API
  slug: cognition-labs-attachments-api
- description: Agent Compute Unit (ACU) usage and billing metrics.
  name: Cognition Labs Consumption API
  slug: cognition-labs-consumption-api
- description: Cross-organization administration.
  name: Cognition Labs Enterprise (v3) API
  slug: cognition-labs-enterprise-v3-api
- description: Organization knowledge entries and folders.
  name: Cognition Labs Knowledge API
  slug: cognition-labs-knowledge-api
- description: Send and read messages within a running session.
  name: Cognition Labs Messages API
  slug: cognition-labs-messages-api
- description: Current org-scoped session and user management.
  name: Cognition Labs Organizations (v3) API
  slug: cognition-labs-organizations-v3-api
- description: Reusable team playbooks that seed new sessions.
  name: Cognition Labs Playbooks API
  slug: cognition-labs-playbooks-api
- description: Encrypted credentials Devin can use inside sessions.
  name: Cognition Labs Secrets API
  slug: cognition-labs-secrets-api
- description: Create and manage Devin sessions (v1 legacy surface).
  name: Cognition Labs Sessions API
  slug: cognition-labs-sessions-api
artifact_total: 18
collections:
- collection_type: open
  name: Devin API (Cognition Labs)
  slug: open-cognition-labs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cognition-labs-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cognition-labs-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cognition-labs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cognition-labs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cognition-labs-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CognitionAI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cognition-ai-labs
- group: company
  title: ''
  type: Website
  url: https://cognition.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.devin.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/cognition-labs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cognition-labs-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cognition-labs-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://cognition.com/blog
created: '2026-07-02'
description: Cognition Labs is the applied AI lab behind Devin, the autonomous AI software engineer that plans, writes, tests, and ships code inside its own shell, code editor, and browser. The Devin API lets teams create and drive Devin sessions programmatically - sending prompts and follow-up messages, attaching files, storing organizational knowledge and reusable playbooks, injecting secrets, and tracking Agent Compute Unit (ACU) consumption - across a legacy v1 surface, a v2 enterprise surface, and a current v3 organizations/enterprise surface built around service-user and personal access tokens.
finops:
- name: Cognition Labs Finops
  service_category: AI and Machine Learning
  slug: cognition-labs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cognition-labs.png
layout: provider
modified: '2026-07-02'
name: Cognition Labs
nav: Providers
network: true
overview: 'Cognition Labs publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Attachments API, Consumption API, Enterprise (v3) API, and 6 more. Tagged areas include AI, AI Agent, Autonomous Coding, Software Engineering, and LLM.


  Cognition Labs'' developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Cognition Labs Plans Pricing
  plan_count: 6
  slug: cognition-labs-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 6
  name: Cognition Labs Rate Limits
  slug: cognition-labs-rate-limits
score:
  band: thin
  composite: 39.2
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 55.5
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Cognition Labs Authentication
  slug: cognition-labs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cognition Labs Domain Security
  slug: cognition-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cognition Labs Vulnerability Disclosure
  slug: cognition-labs-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Cognition Labs Trust Center
  slug: cognition-labs-trust-center
  summary_line: SOC 2, ISO 27001
slug: cognition-labs
tags:
- AI
- AI Agent
- Autonomous Coding
- Software Engineering
- LLM
- Devin
website: https://cognition.ai/
---
