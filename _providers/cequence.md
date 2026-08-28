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
  scored_at: '2026-08-26'
api_count: 5
apis:
- description: API Spyder is a SaaS-based, agentless external discovery service that provides an attacker's view into an organization's public-facing API hosts, hosting providers, and API-specific exposures includin
  name: Cequence API Spyder
  slug: cequence-api-spyder
- description: API Sentinel is the Cequence API posture and compliance module that continuously inventories internal and external APIs, classifies sensitive data flows, scores API risk against governance policies, a
  name: Cequence API Sentinel
  slug: cequence-api-sentinel
- description: API Spartan provides runtime protection against malicious and unwanted API traffic, including account takeover, credential stuffing, scraping, gift-card fraud, and other business logic abuse, with ML-
  name: Cequence API Spartan
  slug: cequence-api-spartan
- description: API Security Testing extends Cequence into shift-left, performing pre-production OpenAPI conformance and vulnerability testing against the OWASP API Security Top 10, feeding results back into Sentinel
  name: Cequence API Security Testing
  slug: cequence-api-security-testing
- description: Cequence Defender is a reverse-proxy deployed inline with API traffic, enforcing API policies, filtering malicious traffic, and providing real-time detection and mitigation through active traffic insp
  name: Cequence Defender
  slug: cequence-defender
artifact_total: 10
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/cequence-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cequence-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cequence-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cequence-security
- group: company
  title: ''
  type: Website
  url: https://www.cequence.ai/
- group: other
  title: ''
  type: Products
  url: https://www.cequence.ai/products/
- group: operate
  title: ''
  type: HelpCenter
  url: https://helpdesk.cequence.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.cequence.ai/blog/
- group: company
  title: ''
  type: News
  url: https://www.cequence.ai/news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cequence.ai/privacy-policy/
- group: agent
  title: ''
  type: LlmsText
  url: https://www.cequence.ai/llms.txt
created: '2025-01-08'
description: Cequence Security delivers the Unified API Protection (UAP) platform, combining external API attack-surface discovery, posture and compliance analysis, inline runtime protection, and testing into a single solution for defending web applications, APIs, and AI endpoints against business logic abuse, bot attacks, and fraud. The Cequence product family is organized into API Spyder (agentless external discovery), API Sentinel (API inventory, posture, and compliance), API Spartan (runtime bot and abuse defense), API Security Testing (shift-left OpenAPI conformance and vulnerability testing), and Cequence Defender (inline reverse-proxy enforcement of API policy).
finops:
- name: Cequence Finops
  service_category: API
  slug: cequence-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cequence.png
layout: provider
modified: '2026-04-23'
name: Cequence Security
nav: Providers
network: true
overview: 'Cequence Security publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Protection, API Discovery, API Security, Application Security, and Attack Surface.


  Cequence Security''s developer surface includes engineering blog, product news, and 9 more developer resources.'
plans:
- name: Cequence Plans Pricing
  plan_count: 3
  slug: cequence-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Cequence Rate Limits
  slug: cequence-rate-limits
score:
  band: emerging
  composite: 16.7
  delta: 2.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 14.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cequence/refs/heads/main/screenshots/cequence-2026-06-20T174136.png
security:
- kind: domain-security
  name: Cequence Domain Security
  slug: cequence-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cequence Trust Center
  slug: cequence-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: cequence
tags:
- AI Protection
- API Discovery
- API Security
- Application Security
- Attack Surface
- Bot Management
- Business Logic Abuse
- CNAPP
- Cybersecurity
- Fraud
- Unified API Protection
website: https://www.cequence.ai/
---
