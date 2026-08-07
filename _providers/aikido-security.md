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
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Aikido Security Agentic Access
  operation_count: 50
  slug: aikido-security-agentic-access
  summary_line: 50 operations · 24 acting
api_count: 12
apis:
- description: The Clouds API from Aikido Security — 7 operation(s) for clouds.
  name: Aikido Security Clouds API
  slug: aikido-security-clouds-api
- description: The Code Repositories API from Aikido Security — 4 operation(s) for code repositories.
  name: Aikido Security Code Repositories API
  slug: aikido-security-code-repositories-api
- description: The Compliance API from Aikido Security — 5 operation(s) for compliance.
  name: Aikido Security Compliance API
  slug: aikido-security-compliance-api
- description: The Containers API from Aikido Security — 3 operation(s) for containers.
  name: Aikido Security Containers API
  slug: aikido-security-containers-api
- description: The Custom Rules API from Aikido Security — 2 operation(s) for custom rules.
  name: Aikido Security Custom Rules API
  slug: aikido-security-custom-rules-api
- description: The Domains API from Aikido Security — 3 operation(s) for domains.
  name: Aikido Security Domains API
  slug: aikido-security-domains-api
- description: The Issues API from Aikido Security — 6 operation(s) for issues.
  name: Aikido Security Issues API
  slug: aikido-security-issues-api
- description: The Teams API from Aikido Security — 2 operation(s) for teams.
  name: Aikido Security Teams API
  slug: aikido-security-teams-api
- description: The Users API from Aikido Security — 2 operation(s) for users.
  name: Aikido Security Users API
  slug: aikido-security-users-api
- description: The Webhooks API from Aikido Security — 2 operation(s) for webhooks.
  name: Aikido Security Webhooks API
  slug: aikido-security-webhooks-api
- description: The Workspace API from Aikido Security — 2 operation(s) for workspace.
  name: Aikido Security Workspace API
  slug: aikido-security-workspace-api
- description: The Zen API from Aikido Security — 2 operation(s) for zen.
  name: Aikido Security Zen API
  slug: aikido-security-zen-api
artifact_total: 21
collections:
- collection_type: open
  name: Aikido Security Public REST API
  slug: open-aikido-security
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aikido-security-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/aikido-security-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aikido-security-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aikido-security-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aikido-security-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.aikido.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://help.aikido.dev/
- group: docs
  title: ''
  type: APIDocumentation
  url: https://apidocs.aikido.dev/
- group: start
  title: ''
  type: Login
  url: https://app.aikido.dev/login
- group: start
  title: ''
  type: Signup
  url: https://app.aikido.dev/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aikido.dev/pricing
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.aikido.dev/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aikido.dev/
- group: company
  title: ''
  type: Blog
  url: https://www.aikido.dev/blog
- group: other
  title: ''
  type: Customers
  url: https://www.aikido.dev/case-studies
- group: company
  title: ''
  type: AboutUs
  url: https://www.aikido.dev/about
- group: company
  title: ''
  type: Careers
  url: https://www.aikido.dev/careers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AikidoSec
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aikido-security/
created: '2026-05-23'
description: Aikido Security is a developer-first all-in-one application security platform that consolidates SAST, SCA, secret detection, container scanning, IaC scanning, CSPM, DAST, API security, malware detection, cloud posture, and AI pentesting into a single product designed for engineering teams. Aikido exposes a public REST API at apidocs.aikido.dev covering issues, code repositories, cloud resources, containers, domains and APIs, compliance (SOC2, ISO 27001, NIS2, CIS), custom SAST rules, AI pentesting, task tracking, webhooks, user and team management, Zen app-protection configuration, and activity logging.
finops:
- name: Aikido Security Finops
  service_category: API
  slug: aikido-security-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aikido-security.png
layout: provider
modified: '2026-05-23'
name: Aikido Security
nav: Providers
network: true
overview: 'Aikido Security publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Clouds API, Code Repositories API, Compliance API, and 9 more. Tagged areas include AI Pentesting, API Security, Application Security, Cloud Security, and Compliance.


  Aikido Security''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, and 14 more developer resources.'
plans:
- name: Aikido Security Plans Pricing
  plan_count: 1
  slug: aikido-security-plans-pricing
random_paper: 89
rate_limits:
- limit_count: 2
  name: Aikido Security Rate Limits
  slug: aikido-security-rate-limits
score:
  band: developing
  composite: 44.1
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 57.4
    developer_ergonomics: 28.3
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 44.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aikido-security/refs/heads/main/screenshots/aikido-security-2026-06-20T170912.png
security:
- kind: authentication
  name: Aikido Security Authentication
  slug: aikido-security-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Aikido Security Domain Security
  slug: aikido-security-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Aikido Security Vulnerability Disclosure
  slug: aikido-security-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
- kind: trust-center
  name: Aikido Security Trust Center
  slug: aikido-security-trust-center
  summary_line: SOC 2, ISO 27001
slug: aikido-security
tags:
- AI Pentesting
- API Security
- Application Security
- Cloud Security
- Compliance
- DAST
- Developer-First
- IaC Scanning
- SAST
- SCA
- Secret Detection
website: https://www.aikido.dev/
---
