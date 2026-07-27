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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Amazon Vpn Agentic Access
  operation_count: 1
  slug: amazon-vpn-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 2
apis:
- description: The AWS VPN API (part of the Amazon EC2 API) provides programmatic access to create and manage VPN connections, customer gateways, virtual private gateways, and Client VPN endpoints. It enables config
  name: AWS VPN API
  slug: aws-vpn-api
- description: The AWS VPN API (Amazon EC2 Query API Subset) API from Amazon VPN — 1 operation(s) for aws vpn api (amazon ec2 query api subset).
  name: Amazon VPN AWS VPN API (Amazon EC2 Query API Subset) API
  slug: amazon-vpn-aws-vpn-api-amazon-ec2-query-api-subset-api
artifact_total: 17
collections:
- collection_type: open
  name: AWS VPN API (Amazon EC2 Query API subset)
  slug: open-amazon-vpn
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-vpn-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-vpn-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-vpn-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-vpn-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-vpn-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/vpn/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/vpn/latest/s2svpn/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/vpc/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: start
  title: ''
  type: Signup
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: start
  title: ''
  type: Login
  url: https://aws.amazon.com/console/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/amazon-vpn/refs/heads/main/rules/amazon-vpn-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/amazon-vpn/refs/heads/main/vocabulary/amazon-vpn-vocabulary.yaml
created: '2026-03-16'
description: 'AWS VPN solutions establish secure connections between on-premises networks, remote offices, client devices, and the AWS global network. AWS offers two types of private connectivity: AWS Site-to-Site VPN and AWS Client VPN, enabling encrypted tunnels between your network and Amazon Virtual Private Cloud.'
examples:
- key_count: 2
  name: Amazon Vpn Example
  slug: amazon-vpn-example
features:
- description: Automate operational tasks with Amazon VPN.
  name: Automation
- description: Programmatic access to Amazon VPN resources.
  name: API Access
finops:
- name: Amazon Vpn Finops
  service_category: API
  slug: amazon-vpn-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-vpn.png
jsonld:
- class_count: 0
  name: Amazon Vpn Context
  property_count: 0
  slug: amazon-vpn-context
layout: provider
modified: '2026-04-19'
name: Amazon VPN
nav: Providers
network: true
overview: 'Amazon VPN publishes 1 API on the [APIs.io](https://apis.io/) network: AWS VPN API (Amazon EC2 Query API Subset) API. Tagged areas include Networking, Security, and VPN.


  The Amazon VPN catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Amazon VPN''s developer surface includes authentication, developer portal, documentation, developer console, support, signup flow, and 12 more developer resources.'
plans:
- name: Amazon Vpn Plans Pricing
  plan_count: 3
  slug: amazon-vpn-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Amazon Vpn Rate Limits
  slug: amazon-vpn-rate-limits
rules:
- name: Amazon VPN API Rules
  rule_count: 11
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 7
  slug: amazon-vpn-spectral-rules
score:
  band: developing
  composite: 59.9
  delta: 3.3
  facets:
    commercial_clarity: 81.6
    contract_quality: 64.6
    developer_ergonomics: 39.1
    discoverability: 80.0
    governance: 39.5
    operational_transparency: 52.6
  previous_composite: 56.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-vpn/refs/heads/main/screenshots/amazon-vpn-2026-06-20T171844.png
security:
- kind: authentication
  name: Amazon Vpn Authentication
  slug: amazon-vpn-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Vpn Domain Security
  slug: amazon-vpn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Vpn Vulnerability Disclosure
  slug: amazon-vpn-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Vpn Trust Center
  slug: amazon-vpn-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-vpn
tags:
- Networking
- Security
- VPN
use_cases:
- description: Use Amazon VPN to manage and automate cloud operations.
  name: Cloud Operations
website: https://aws.amazon.com/vpn/
---
