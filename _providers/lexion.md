---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
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
  score: 19.4
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: 'Centralized intelligent repository for agreements, surfacing contracts, parties, key dates, and metadata. Lexion offers an enterprise integration API to push contract terms and metadata into external '
  name: Lexion Contract Repository
  slug: contract-repository
- description: AI-based extraction of clauses, key terms, renewal dates, and contract insights, plus AI Contract Assist for review against playbooks. Surfaced through the Lexion product and its enterprise integratio
  name: Lexion Extraction & Insights
  slug: extraction-insights
- description: No-code intake, approval, document-generation, and routing workflows, with email-, Slack-, and Microsoft Teams-driven request submission. Workflow automation is configured in-product; no openly docume
  name: Lexion Workflows
  slug: workflows
- description: Pre-built connectors for Email, Microsoft Word, Salesforce, HubSpot, Slack, Microsoft Teams, Coupa, NetSuite, and DocuSign, plus a custom integration API for connecting Lexion to other business system
  name: Lexion Integrations
  slug: integrations
artifact_total: 10
collections:
- collection_type: open
  name: Lexion API
  slug: open-lexion
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/lexion-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lexion-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lexion
- group: company
  title: ''
  type: Website
  url: https://www.lexion.ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.lexion.ai/integrations/api
- group: company
  title: ''
  type: Blog
  url: https://www.lexion.ai/blog
- group: commercial
  title: ''
  type: Plans
  url: plans/lexion-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lexion-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lexion-finops.yml
created: '2026-06-21'
description: Lexion is an AI-powered contract lifecycle management (CLM) platform that centralizes agreements in an intelligent repository, extracts key terms and dates, and drives no-code intake and approval workflows across legal, sales, procurement, finance, and HR. Founded in 2019 out of the Allen Institute for AI, Lexion was acquired by Docusign in May 2024 for ~$165M and folded into Docusign's Intelligent Agreement Management (IAM) platform and Docusign Navigator. Lexion exposes an enterprise, sales-led integration API but does not publish a self-serve, openly documented public API.
finops:
- name: Lexion Finops
  service_category: Software as a Service
  slug: lexion-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lexion.png
layout: provider
modified: '2026-06-21'
name: Lexion
nav: Providers
network: true
overview: 'Lexion publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Contract Repository, Extraction & Insights, Workflows, and 1 more. Tagged areas include Contract Management, CLM, AI, Legal Tech, and Document Extraction.


  Lexion''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Lexion Plans Pricing
  plan_count: 1
  slug: lexion-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 1
  name: Lexion Rate Limits
  slug: lexion-rate-limits
score:
  band: emerging
  composite: 26.8
  delta: -3.7
  facets:
    commercial_clarity: 36.8
    contract_quality: 32.3
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 30.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lexion/refs/heads/main/screenshots/lexion-2026-07-25T224955.png
security:
- kind: domain-security
  name: Lexion Domain Security
  slug: lexion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Lexion Trust Center
  slug: lexion-trust-center
  summary_line: SOC 2, ISO 27001
slug: lexion
tags:
- Contract Management
- CLM
- AI
- Legal Tech
- Document Extraction
- Workflow
website: https://www.lexion.ai
---
