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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Amazon Vpn Agentic Access
  operation_count: 1
  slug: amazon-vpn-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The AWS VPN API (part of the Amazon EC2 API) provides programmatic access to create and manage VPN connections, customer gateways, virtual private gateways, and Client VPN endpoints. It enables config
  name: AWS VPN API
  slug: aws-vpn-api
- description: The AWS VPN API (Amazon EC2 Query API Subset) API from Amazon VPN — 1 operation(s) for aws vpn api (amazon ec2 query api subset).
  name: Amazon VPN AWS VPN API (Amazon EC2 Query API Subset) API
  slug: amazon-vpn-aws-vpn-api-amazon-ec2-query-api-subset-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AWS VPN API (Amazon EC2 Query API subset) AWS VPN API (Amazon EC2 Query API Subset) AWS VPN API (Amazon EC2 Query API Subset) AWS VPN API (Amazon EC2 Query API Subset) API
  slug: open-amazon-vpn-aws-vpn-api-amazon-ec2-query-api-subset-api
- collection_type: open
  name: AWS VPN API (Amazon EC2 Query API subset)
  slug: open-amazon-vpn
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/amazon-vpn-capability-edges.yml
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


  Amazon VPN''s developer surface includes authentication, developer portal, documentation, developer console, support, signup flow, and 13 more developer resources.'
plans:
- name: Amazon Vpn Plans Pricing
  plan_count: 3
  slug: amazon-vpn-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Amazon Vpn Rate Limits
  slug: amazon-vpn-rate-limits
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Amazon VPN API Rules
  rule_count: 11
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 7
  slug: amazon-vpn-spectral-rules
score:
  band: developing
  composite: 52.4
  coverage:
    artifact_dirs: 15
    catalog_gap: 60.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 26.5
    contract_quality: 60.5
    developer_ergonomics: 61.9
    discoverability: 59.3
    governance: 26.5
    operational_transparency: 26.3
  previous_composite: 52.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
