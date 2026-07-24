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
- acting_count: 11
  human_in_the_loop: 0
  name: Cloudguard Agentic Access
  operation_count: 17
  slug: cloudguard-agentic-access
  summary_line: 17 operations · 11 acting
api_count: 9
apis:
- description: Workload protection capabilities exposed through the CloudGuard platform for Kubernetes admission control, image assurance/CI scanning, runtime protection, and serverless function security.
  name: CloudGuard Workload Protection (CWPP) API
  slug: cloudguard-workload-api
- description: CloudGuard Code Security (formerly Spectral) provides developer-first SAST, infrastructure-as-code scanning, secrets detection, and SCA via CLI and API integrations into CI/CD pipelines.
  name: CloudGuard Code Security (Spectral) API
  slug: cloudguard-code-security-api
- description: CloudGuard WAF (CloudGuard AppSec) protects web applications and APIs with contextual machine-learning-based threat prevention; the platform exposes management APIs for policy, asset, and event config
  name: CloudGuard WAF API
  slug: cloudguard-waf-api
- description: CloudGuard Network Security delivers cloud-native firewalling and threat prevention with management APIs for gateway provisioning, rule management, and integrations with CI/CD pipelines.
  name: CloudGuard Network Security API
  slug: cloudguard-network-security-api
- description: The CloudAccounts API from CloudGuard — 4 operation(s) for cloudaccounts.
  name: CloudGuard CloudAccounts API
  slug: cloudguard-cloudaccounts-api
- description: The Compliance API from CloudGuard — 1 operation(s) for compliance.
  name: CloudGuard Compliance API
  slug: cloudguard-compliance-api
- description: The Findings API from CloudGuard — 5 operation(s) for findings.
  name: CloudGuard Findings API
  slug: cloudguard-findings-api
- description: The Notifications API from CloudGuard — 2 operation(s) for notifications.
  name: CloudGuard Notifications API
  slug: cloudguard-notifications-api
- description: The Policies API from CloudGuard — 1 operation(s) for policies.
  name: CloudGuard Policies API
  slug: cloudguard-policies-api
artifact_total: 18
collections:
- collection_type: open
  name: Check Point CloudGuard CNAPP REST API
  slug: open-cloudguard
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudguard-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudguard-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudguard-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.checkpoint.com/cloudguard/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cgn.portal.checkpoint.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cgn.portal.checkpoint.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://sc1.checkpoint.com/documents/CloudGuard_Dome9/Documentation/Getting-Started/Getting-started-with-CloudGuard.htm
- group: auth
  title: ''
  type: Authentication
  url: https://sc1.checkpoint.com/documents/CloudGuard_Dome9/Documentation/API-Authentication.html
- group: operate
  title: ''
  type: Support
  url: https://support.checkpoint.com/
- group: operate
  title: ''
  type: Community
  url: https://community.checkpoint.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dome9.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.checkpoint.com/privacy/
- group: other
  title: ''
  type: Terraform Provider
  url: https://registry.terraform.io/providers/dome9/dome9/latest/docs
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cloudguard-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/cloudguard-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.checkpoint.com/feed/
created: '2024-01-01'
description: Check Point CloudGuard is a Cloud Native Application Protection Platform (CNAPP) that delivers cloud security posture management (CSPM), cloud workload protection (CWPP), code security, network security, and intelligence/CDR capabilities across AWS, Azure, GCP, Alibaba, Oracle, Kubernetes, and on-premises environments. The CloudGuard public REST API (originally Dome9) is used to onboard cloud accounts, run posture assessments, manage compliance bundles, retrieve findings, and configure policies and alerts.
finops:
- name: Cloudguard Finops
  service_category: API
  slug: cloudguard-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudguard.png
jsonld:
- class_count: 0
  name: Cloudguard Context
  property_count: 5
  slug: cloudguard-context
layout: provider
modified: '2026-04-26'
name: CloudGuard
nav: Providers
network: true
overview: 'CloudGuard publishes 5 APIs on the [APIs.io](https://apis.io/) network, including CloudAccounts API, Compliance API, Findings API, and 2 more. Tagged areas include Check Point, CNAPP, Cloud Security, Compliance, and CSPM.


  The CloudGuard catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CloudGuard''s developer surface includes authentication, documentation, getting-started guide, support, engineering blog, and 11 more developer resources.'
plans:
- name: Cloudguard Plans Pricing
  plan_count: 3
  slug: cloudguard-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 5
  name: Cloudguard Rate Limits
  slug: cloudguard-rate-limits
rules:
- name: CloudGuard API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 5
  slug: cloudguard-rules
score:
  band: developing
  composite: 49.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 55.8
    developer_ergonomics: 45.7
    discoverability: 67.5
    governance: 26.3
    operational_transparency: 47.4
  previous_composite: 49.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudguard/refs/heads/main/screenshots/cloudguard-2026-06-20T174606.png
security:
- kind: authentication
  name: Cloudguard Authentication
  slug: cloudguard-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cloudguard Domain Security
  slug: cloudguard-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cloudguard
tags:
- Check Point
- CNAPP
- Cloud Security
- Compliance
- CSPM
- CWPP
- Posture Management
website: https://www.checkpoint.com/cloudguard/
---
