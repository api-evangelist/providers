---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.0
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 14
  human_in_the_loop: 2
  name: Cognition Agentic Access
  operation_count: 23
  slug: cognition-agentic-access
  summary_line: 23 operations · 14 acting · 2 human-in-the-loop
api_count: 8
apis:
- description: The Devin API is a REST interface for creating and managing autonomous engineering sessions, knowledge, playbooks, secrets, and analytics across an organization or enterprise. It lets developers progr
  name: Devin API
  slug: devin-api
- description: Operations for file uploads
  name: Cognition AI Attachments API
  slug: cognition-attachments-api
- description: Operations for managing audit logs
  name: Cognition AI AuditLogs API
  slug: cognition-auditlogs-api
- description: Operations for enterprise-specific features and reporting
  name: Cognition AI Enterprise API
  slug: cognition-enterprise-api
- description: Operations for managing knowledge
  name: Cognition AI Knowledge API
  slug: cognition-knowledge-api
- description: Operations for managing playbooks
  name: Cognition AI Playbooks API
  slug: cognition-playbooks-api
- description: Operations for managing secrets and credentials
  name: Cognition AI Secrets API
  slug: cognition-secrets-api
- description: Operations for creating and managing Devin sessions
  name: Cognition AI Sessions API
  slug: cognition-sessions-api
artifact_total: 17
collections:
- collection_type: open
  name: Devin External API
  slug: open-cognition
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cognition-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cognition-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cognition-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cognition-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cognition-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://cognition.ai
- group: other
  title: ''
  type: ProductSite
  url: https://devin.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.devin.ai
- group: company
  title: ''
  type: Blog
  url: https://cognition.ai/blog
- group: other
  title: ''
  type: Research
  url: https://cognition.ai/research
- group: commercial
  title: ''
  type: Pricing
  url: https://devin.ai/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.devin.ai/signup
- group: start
  title: ''
  type: Login
  url: https://app.devin.ai/login
- group: company
  title: ''
  type: Careers
  url: https://cognition.ai/careers
- group: operate
  title: ''
  type: Contact
  url: https://cognition.ai/contact
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.devin.ai/release-notes/overview
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cognition-ai-labs
- group: company
  title: ''
  type: Twitter
  url: https://x.com/cognition
created: '2026-05-23'
description: Cognition AI is an applied AI lab building Devin, an autonomous AI software engineer that plans, writes, tests, and ships production code. The company also operates the Windsurf agentic IDE following its 2025 acquisition of the Windsurf team and product. Devin is sold to individual developers, engineering teams, and enterprises as a managed agent that integrates with GitHub, Linear, Slack, Jira, and CI systems to handle migrations, PR review, bug triage, documentation, and scheduled engineering work. Cognition exposes a v3 REST API (Organization and Enterprise scopes) plus a CLI so customers can program Devin into their own workflows. Pricing runs from a free tier through Pro ($20/mo), Max ($200/mo), Teams ($80/seat/mo), and custom Enterprise plans with SAML/OIDC SSO and VPC deployment.
finops:
- name: Cognition Finops
  service_category: API
  slug: cognition-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cognition.png
layout: provider
modified: '2026-05-23'
name: Cognition AI
nav: Providers
network: true
overview: 'Cognition AI publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Attachments API, AuditLogs API, Enterprise API, and 4 more. Tagged areas include Autonomous Agents, AI Software Engineer, Coding Agents, Developer Productivity, and DevOps.


  Cognition AI''s developer surface includes authentication, documentation, engineering blog, pricing, signup flow, release notes, and 12 more developer resources.'
plans:
- name: Cognition Plans Pricing
  plan_count: 1
  slug: cognition-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Cognition Rate Limits
  slug: cognition-rate-limits
score:
  band: developing
  composite: 43.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 58.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 43.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cognition/refs/heads/main/screenshots/cognition-2026-06-20T174713.png
security:
- kind: authentication
  name: Cognition Authentication
  slug: cognition-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cognition Domain Security
  slug: cognition-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cognition Vulnerability Disclosure
  slug: cognition-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Cognition Trust Center
  slug: cognition-trust-center
  summary_line: SOC 2, ISO 27001
slug: cognition
tags:
- Autonomous Agents
- AI Software Engineer
- Coding Agents
- Developer Productivity
- DevOps
- Code Migration
- Code Review
- GitHub Integration
- Enterprise AI
- Agentic Workflows
- IDE
- LLM Applications
website: https://cognition.ai
---
