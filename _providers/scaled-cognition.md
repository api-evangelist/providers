---
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
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The stateless RESTful API behind the Scaled Cognition Agent Builder platform, used to author, simulate, deploy and monitor APT-1 agents. Scaled Cognition describes the interface publicly as an open, v
  name: Scaled Cognition APT Agent Platform API
  slug: scaled-cognition-apt-agent-platform-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.scaledcognition.com
- group: company
  title: ''
  type: About
  url: https://www.scaledcognition.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.scaledcognition.com/resources
- group: operate
  title: ''
  type: StatusPage
  url: https://status.scaledcognition.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.scaledcognition.com
- group: auth
  title: ''
  type: Compliance
  url: conformance/scaled-cognition-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/scaled-cognition-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/scaled-cognition-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scaled-cognition-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/scaled-cognition-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/scaled-cognition-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/scaled-cognition-rate-limits.yml
- group: start
  title: ''
  type: Login
  url: https://studio.scaledcognition.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.scaledcognition.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.scaledcognition.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ScaledCognition
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/scaledcognition/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/ScaledCognition
- group: company
  title: ''
  type: Careers
  url: https://www.scaledcognition.com/careers
coverage:
  checked: '2026-08-26'
  detail: Scaled Cognition's Agent Builder API demonstrably ships an OpenAPI — https://studio.scaledcognition.com/api/openapi.json answers 401 {"error":"Not authenticated."} rather than 404 — but every reference path on that host 307-redirects to /login, docs.scaledcognition.com does not resolve, api.scaledcognition.com 403s every anonymous request from an AWS ELB, and the marketing site has no developer section at all, so the contract is readable only by an existing tenant.
  evidence:
  - status: 401
    url: https://studio.scaledcognition.com/api/openapi.json
  - status: 307
    url: https://studio.scaledcognition.com/docs
  - status: 403
    url: https://api.scaledcognition.com/openapi.json
  - status: 404
    url: https://www.scaledcognition.com/openapi.json
  reason: customer-only-docs
  state: gated
created: '2026-08-26'
description: Scaled Cognition is a Mountain View, California AI model lab and enterprise platform company behind APT-1, the Agentic Pretrained Transformer — a frontier model the company says is pretrained on action prediction rather than token prediction and purpose-built for enterprise customer-experience agents. The commercial surface is an Agent Builder platform (Studio, a Python APT SDK, AgentTwin transcript-to-agent conversion, GenAPI simulation, Agent Evaluator, Agent Monitor and Agent Defender) exposed to customers through a stateless RESTful API that can run in Scaled Cognition's SOC 2 Type II cloud, in a customer VPC, or on-premises. Founded by Dan Roth (CEO), Dan Klein (CTO, UC Berkeley) and Damon Pender (CFO), the team previously built Semantic Machines, acquired by Microsoft in 2018. Backed by Khosla Ventures with a Genesys partnership. No public developer portal, API reference, or machine-readable contract is published — the platform API and its OpenAPI live behind the Studio
  login.
image: https://cdn.prod.website-files.com/695bbfca07da756ac77e9b23/69f0d4e5f4a9f3085d8c4f7c_webclip.png
layout: provider
modified: '2026-08-26'
name: Scaled Cognition
nav: Providers
network: true
overview: 'Scaled Cognition publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Agents, Large Language Models, Customer Experience, and Contact Center.


  Scaled Cognition''s developer surface includes engineering blog and 18 more developer resources.'
plans:
- name: Scaled Cognition Plans Pricing
  plan_count: 0
  slug: scaled-cognition-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Scaled Cognition Rate Limits
  slug: scaled-cognition-rate-limits
score:
  band: emerging
  composite: 19.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 18.4
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: domain-security
  name: Scaled Cognition Domain Security
  slug: scaled-cognition-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: trust-center
  name: Scaled Cognition Trust Center
  slug: scaled-cognition-trust-center
  summary_line: trust center published
slug: scaled-cognition
tags:
- Artificial Intelligence
- Agents
- Large Language Models
- Customer Experience
- Contact Center
- Conversational AI
- Voice
- Enterprise Software
- Machine Learning
- Company
website: https://www.scaledcognition.com
---
