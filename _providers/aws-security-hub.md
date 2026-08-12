---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 27
  human_in_the_loop: 3
  name: Aws Security Hub Agentic Access
  operation_count: 40
  slug: aws-security-hub-agentic-access
  summary_line: 40 operations · 27 acting · 3 human-in-the-loop
api_count: 12
apis:
- description: 'REST API for managing security standards, controls, findings, insights, automation rules, and member account configuration in AWS Security Hub. Requests are authenticated with AWS Signature Version 4 '
  name: AWS Security Hub CSPM API
  slug: cspm-api
- description: The Action Targets API from AWS Security Hub — 1 operation(s) for action targets.
  name: AWS Security Hub Action Targets API
  slug: aws-security-hub-action-targets-api
- description: The Automation Rules API from AWS Security Hub — 4 operation(s) for automation rules.
  name: AWS Security Hub Automation Rules API
  slug: aws-security-hub-automation-rules-api
- description: The Configuration Policies API from AWS Security Hub — 3 operation(s) for configuration policies.
  name: AWS Security Hub Configuration Policies API
  slug: aws-security-hub-configuration-policies-api
- description: The Controls API from AWS Security Hub — 3 operation(s) for controls.
  name: AWS Security Hub Controls API
  slug: aws-security-hub-controls-api
- description: The Findings API from AWS Security Hub — 3 operation(s) for findings.
  name: AWS Security Hub Findings API
  slug: aws-security-hub-findings-api
- description: The Hub API from AWS Security Hub — 1 operation(s) for hub.
  name: AWS Security Hub Hub API
  slug: aws-security-hub-hub-api
- description: The Insights API from AWS Security Hub — 4 operation(s) for insights.
  name: AWS Security Hub Insights API
  slug: aws-security-hub-insights-api
- description: The Invitations API from AWS Security Hub — 3 operation(s) for invitations.
  name: AWS Security Hub Invitations API
  slug: aws-security-hub-invitations-api
- description: The Members API from AWS Security Hub — 4 operation(s) for members.
  name: AWS Security Hub Members API
  slug: aws-security-hub-members-api
- description: The Standards API from AWS Security Hub — 4 operation(s) for standards.
  name: AWS Security Hub Standards API
  slug: aws-security-hub-standards-api
- description: The Tags API from AWS Security Hub — 1 operation(s) for tags.
  name: AWS Security Hub Tags API
  slug: aws-security-hub-tags-api
artifact_total: 18
collections:
- collection_type: open
  name: AWS Security Hub API
  slug: open-aws-security-hub
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aws-security-hub-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/aws-security-hub-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aws-security-hub-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aws-security-hub-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aws-security-hub-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/security-hub/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/securityhub/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/security-hub/pricing/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/security/feed/
created: '2026-05-11'
description: AWS Security Hub is a cloud security posture management (CSPM) service that aggregates, organizes, and prioritizes security findings from AWS services like Amazon GuardDuty, Inspector, and Macie, as well as supported third-party products. It continuously assesses your AWS environment against security standards such as AWS Foundational Security Best Practices, CIS, PCI DSS, and NIST. The Security Hub API and AWS SDKs provide access to findings, controls, insights, and automation rules using AWS Signature Version 4 authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aws-security-hub.png
layout: provider
modified: '2026-05-11'
name: AWS Security Hub
nav: Providers
network: true
overview: 'AWS Security Hub publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Action Targets API, Automation Rules API, Configuration Policies API, and 8 more. Tagged areas include Security, Cloud Security Posture Management, Compliance, Findings, and Threat Detection.


  AWS Security Hub''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 5 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 31.1
  delta: 2.1
  facets:
    commercial_clarity: 31.6
    contract_quality: 52.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 29.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aws-security-hub/refs/heads/main/screenshots/aws-security-hub-2026-06-20T172802.png
security:
- kind: authentication
  name: Aws Security Hub Authentication
  slug: aws-security-hub-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aws Security Hub Domain Security
  slug: aws-security-hub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aws Security Hub Vulnerability Disclosure
  slug: aws-security-hub-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Aws Security Hub Trust Center
  slug: aws-security-hub-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: aws-security-hub
tags:
- Security
- Cloud Security Posture Management
- Compliance
- Findings
- Threat Detection
- Cloud
website: https://aws.amazon.com/security-hub/
---
