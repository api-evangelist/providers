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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 3
apis:
- description: Augmentt Discover provides SaaS discovery and Shadow IT detection capabilities for MSPs, identifying all cloud applications used across managed client environments.
  name: Augmentt Discover
  slug: augmentt-discover
- description: Augmentt Optimize tracks SaaS usage and spend across client environments to identify unused licenses, redundant applications, and cost savings opportunities for MSPs.
  name: Augmentt Optimize
  slug: augmentt-optimize
- description: Augmentt Engage provides SaaS administration, management, and automation capabilities allowing MSPs to centralize SaaS security policy enforcement and user lifecycle management across Microsoft 365 an
  name: Augmentt Engage
  slug: augmentt-engage
artifact_total: 20
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/augmentt-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/augmentt-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Augmentt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/augmentt
- group: company
  title: ''
  type: Website
  url: https://www.augmentt.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.augmentt.com/resources
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.augmentt.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.augmentt.com/terms-of-service/
- group: operate
  title: ''
  type: Contact
  url: https://www.augmentt.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.augmentt.com/blog/
- group: start
  title: ''
  type: Signup
  url: https://www.augmentt.com/free-trial/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.augmentt.com/pricing/
- group: agent
  title: ''
  type: LlmsText
  url: https://augmentt.com/llms.txt
created: '2026-03-27'
description: Augmentt is a multi-tenant SaaS management platform built for managed service providers (MSPs). It provides SaaS discovery (Shadow IT), license optimization, usage tracking, spend management, and SaaS security policy enforcement across Microsoft 365 and cloud applications. Augmentt integrates with major PSA and RMM platforms including ConnectWise and N-able.
features:
- description: Manage SaaS applications across multiple client tenants from a single MSP dashboard with hierarchical access control.
  name: Multi-Tenant Management
- description: Automatically discover all cloud applications in use across client environments including Shadow IT not approved by IT.
  name: SaaS Discovery
- description: Track license utilization, identify unused seats, and generate recommendations to reduce SaaS spend across clients.
  name: License Optimization
- description: Enforce security policies across SaaS applications including MFA requirements, conditional access, and app permissions.
  name: SaaS Security Policies
- description: Automate user onboarding and offboarding across SaaS applications when employees join or leave client organizations.
  name: User Lifecycle Management
- description: Integrate discovery and optimization data with PSA platforms for automated billing and service delivery.
  name: PSA Integration
finops:
- name: Augmentt Finops
  service_category: API
  slug: augmentt-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/augmentt.png
layout: provider
modified: '2026-04-19'
name: Augmentt
nav: Providers
network: true
overview: 'Augmentt publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include MSP, Microsoft 365, SaaS Management, SaaS Security, and Shadow IT.


  Augmentt''s developer surface includes documentation, engineering blog, signup flow, pricing, and 9 more developer resources.'
plans:
- name: Augmentt Plans Pricing
  plan_count: 3
  slug: augmentt-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 5
  name: Augmentt Rate Limits
  slug: augmentt-rate-limits
score:
  band: emerging
  composite: 24.1
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 24.1
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/augmentt/refs/heads/main/screenshots/augmentt-2026-07-25T201708.png
security:
- kind: domain-security
  name: Augmentt Domain Security
  slug: augmentt-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Augmentt Vulnerability Disclosure
  slug: augmentt-vulnerability-disclosure
  summary_line: disclosure policy published
slug: augmentt
solutions:
- description: Package and deliver SaaS management as a managed service offering including discovery, optimization, and security monitoring.
  name: MSP SaaS Management Service
- description: Extend M365 security posture management with SaaS-specific controls, policy enforcement, and compliance reporting.
  name: Microsoft 365 Security
tags:
- MSP
- Microsoft 365
- SaaS Management
- SaaS Security
- Shadow IT
use_cases:
- description: Identify and eliminate wasted SaaS spend by discovering unused licenses and redundant applications across client portfolios.
  name: SaaS Spend Management
- description: Detect and manage unsanctioned cloud applications to reduce security risk and enforce acceptable use policies.
  name: Shadow IT Control
- description: Manage M365 licenses, security settings, and user access across all client tenants from a unified MSP console.
  name: Microsoft 365 Management
- description: Automate secure offboarding of departing employees by revoking access to all SaaS applications simultaneously.
  name: Employee Offboarding
website: https://www.augmentt.com
---
